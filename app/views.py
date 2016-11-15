from app import app
from flask import render_template, request, flash, redirect
from app import mongo,communicator
from datetime import datetime
import pymongo



@app.route('/')
def index():
    #client=mongo.connect()
    return render_template("index.html",title="Welcome to vicblog!",page_name="index")

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
        submit = communicator.LoginSubmit(login_package)
        return submit.execute()
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
        submit = communicator.RegisterSubmit(register_package)
        return submit.execute()

    else:
        return render_template("register.html",title="Register",page_name="Register")

@app.route('/about')
def about():
    return render_template("about.html",page_name="about")