from app import app
from flask import render_template, request, flash, redirect, Response, make_response, Markup, g, url_for
from app import submits,user,database
from datetime import datetime
import pymongo, json, os
from werkzeug import secure_filename
from markdown2 import Markdown

@app.before_request
def before_request():
    token=request.cookies.get("login")
    current_user = user.User.create_from_token(token)
    g.user = current_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        login_package={
            'username':request.form['form_user'], 
            'password': request.form['form_password'],
            'role':"user", 
        }
        submit = submits.LoginSubmit(login_package)
        status_code, token = submit.execute()
        
        return_dict={
            "status_code": status_code, 
            "token": token, 
            "user": user.User.create_from_token(token), 
        }

        return json.dumps(return_dict,cls=user.UserEncoder)
    else:
        return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        register_package={
            'username':request.form['form_user'], 
            'password':request.form['form_password'], 
            'role':'user', 
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
    articles=[]
    for article in database.find("articles",None):
        articles.append({
            "id":article["id"], 
            "username":article["username"],  
            "content":Markup(article["content"]),
            "submit_time":article["submit_time"],
            "title":article["title"], 
        })
    return render_template("articles.html",articles=articles)

@app.route('/compose',methods=["GET","POST"])
def compose():
    if request.method=="GET":
        if g.user==None or (g.user!=None and g.user.role=="user"):
            return redirect(url_for("login"))
        return render_template("compose.html")
    else:
        markdownor = Markdown()
        package={
            "username": g.user.username, 
            "content": markdownor.convert(request.form["content"]), 
            "title": request.form["title"], 
            "categories":["test"], 
        }
        article = submits.ArticleSubmit(package)
        article.execute()
        return json.dumps({
            "status":"success",
        })
        
@app.route('/articles/<article_id>')
def view_article(article_id):
    article = database.find_one("articles",{"id":article_id})
    article["content"] = Markup(article["content"])
    return render_template("article.html",article=article)

    
@app.route('/upload',methods=["POST"])
def upload():
    f= request.files["img_upload"]
    filename=""
    if f:          
        filename=secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return_package={
        "status":"success",
        "filename": filename,  
        "url":os.path.join(app.config['UPLOAD_FOLDER'], filename).replace("app/",""), 
    }
    return json.dumps(return_package)