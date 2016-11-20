from app import app
from flask import render_template, request, flash, redirect, Response, make_response, Markup, g, url_for
from app import submits,user,controllers
from datetime import datetime
import pymongo

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
            'username':request.form['user'], 
            'password': request.form['password'],
            'role':"user", 
        }
        submit = submits.LoginSubmit(login_package)
        status_code, token = submit.execute()
        if status_code==200:
            resp=make_response(redirect("/"))
            resp.set_cookie("login", token)
            return resp
        if status_code==402:
            return redirect("/login")
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
        if g.user==None:
            return redirect(url_for("login"))
        return render_template("compose.html",title="Compose")
    else:
        pass