from app import app
from flask import render_template, request, flash, redirect, Response, make_response, Markup, g, url_for
from app import submits,user,controllers
from datetime import datetime
import pymongo, json

@app.before_request
def before_request():
    controllers.check_login()

@app.route("/")
def index():
    return render_template("index.html",title="Welcome to vicblog!",page_name="index")

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
        return render_template("login.html",title="Login",page_name="login")

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
        return render_template("register.html",title="Register",page_name="Register")

@app.route('/about')
def about():
    return render_template("about.html",page_name="about")

@app.route('/logout')
def logout():
    resp=make_response(redirect("/"))
    resp.set_cookie("login","")
    return resp

@app.route('/articles')
def articles():
    articles=controllers.acquire_articles()
    return render_template("articles.html",page_name="articles",articles=articles)

@app.route('/compose',methods=["GET","POST"])
def compose():
    if request.method=="GET":
        if g.user==None or (g.user!=None and g.user.role=="user"):
            return redirect(url_for("login"))
        return render_template("compose.html",title="Compose")
    else:
        pass