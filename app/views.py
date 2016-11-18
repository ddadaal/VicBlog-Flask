from app import app
from flask import render_template, request, flash, redirect, Response, make_response
from app import mongo,submits,user
from datetime import datetime
import pymongo


@app.route("/")
def index():
    token=request.cookies.get("login")
    current_user = user.User.create_from_token(token)
    return render_template("index.html",title="Welcome to vicblog!",page_name="index",User=current_user)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        login_package={
            'username':request.form['user'], 
            'password': request.form['password'],
            'role':"user", 
        }

        #register_package={
        #    'name':request.form['name'],
        #    'sign_up_time':datetime.strftime(datetime.utcnow(),"%a, %d %b %Y %H:%M:%S GMT"),
        #    'role':'user',
       # }
       # return str(register_package)
        submit = submits.LoginSubmit(login_package)
        status_code, token = submit.execute()
        if status_code==200:
            resp=make_response(redirect("/"))
            resp.set_cookie("login", token)
            return resp
        if status_code==402:
            redirect("/login")
    else:
        return render_template("login.html",title="Login",page_name="login")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        register_package={
            'username':request.form['user'], 
            'password':request.form['password'], 
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