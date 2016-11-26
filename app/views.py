from app import app
from flask import render_template, request, flash, redirect, Response, make_response, Markup, g, url_for
from app import submits,user,controllers
from datetime import datetime
import pymongo, json, os
from werkzeug import secure_filename

@app.before_request
def before_request():
    controllers.check_login()

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
    articles=controllers.acquire_articles()
    return render_template("articles.html",articles=articles)

@app.route('/compose',methods=["GET","POST"])
def compose():
    if request.method=="GET":
        if g.user==None or (g.user!=None and g.user.role=="user"):
            return redirect(url_for("login"))
        return render_template("compose.html")
    else:
        for uploaded in request.files:
            filename=secure_filename(uploaded.filename)
            uploaded.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
