from app import app
from flask import render_template, request, flash, redirect, Response, make_response, g, url_for
from app import submits, user, database
from datetime import datetime
import pymongo
import json
import os
from flask_cors import CORS, cross_origin
from werkzeug import secure_filename

@app.route("/api/login",methods=["GET","POST"])
def api_login():
    if request.method == "GET":
        return json.dumps({"status":"post here"})

    login_package = {
            'username': request.json['username'],
            'password': request.json['password'],
            'role': "user",
        }
    submit = submits.LoginSubmit(login_package)
    status, token = submit.execute()

    return_dict = {
            "status": status,
            "token": token,
            "user": user.User.create_from_token(token),
    }
    return json.dumps(return_dict,ensure_ascii=False,cls=user.UserEncoder)


@app.route("/api/articles")
def api_articles():
    articles = []
    for article in database.find("articles", None):
        articles.append(submits.format_article(article))
    return json.dumps(articles, ensure_ascii=False)

@app.route("/api/register",methods=["GET","POST"])
def api_register():
    if request.method == "GET":
        return json.dumps({"status":"post here"})

    register_package = {
            'username': request.json['username'],
            'password': request.json['password'],
            'role': 'user',
        }
    submit = submits.RegisterSubmit(register_package)
    result= submit.execute()
    return json.dumps({"status":result})

@app.route("/api/articles/<id>")
def api_view_article(id):
    article = database.find_one("articles", {"id": id})
    return json.dumps(submits.format_article(article),ensure_ascii=False)

@app.before_request
def before_request():
    token = request.cookies.get("login")
    current_user = user.User.create_from_token(token)
    g.user = current_user


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_package = {
            'username': request.form['form_user'],
            'password': request.form['form_password'],
            'role': "user",
        }
        submit = submits.LoginSubmit(login_package)
        status_code, token = submit.execute()

        return_dict = {
            "status_code": status_code,
            "token": token,
            "user": user.User.create_from_token(token),
        }

        return json.dumps(return_dict, cls=user.UserEncoder)
    else:
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        register_package = {
            'username': request.form['form_user'],
            'password': request.form['form_password'],
            'role': 'user',
        }
        submit = submits.RegisterSubmit(register_package)
        return submit.execute()
    else:
        return render_template("register.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/articles')
def articles():
    articles = []
    for article in database.find("articles", None):
        articles.append(submits.format_article(article))
    return render_template("articles.html", articles=articles)


@app.route('/compose', methods=["GET", "POST"])
def compose():
    if request.method == "GET":
        if g.user == None or (g.user != None and g.user.role == "user"):
            return redirect(url_for("login"))
        return render_template("compose.html")
    else:

        package = {
            "username": g.user.username,
            "content": request.form["content"],
            "title": request.form["title"],
            "categories": ["test"],
        }
        article = submits.ArticleSubmit(package)
        article.execute()
        return json.dumps({
            "status": "success",
        })


@app.route('/articles/<article_id>')
def view_article(article_id):
    article = database.find_one("articles", {"id": article_id})
    return render_template("article.html", article=submits.format_article(article))


@app.route('/upload', methods=["POST"])
def upload():
    f = request.files["img_upload"]
    filename = ""
    if f:
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return_package = {
        "status": "success",
        "filename": filename,
        "url": url_for('static', filename="upload/" + filename)
    }
    return json.dumps(return_package)
