from app import app
from flask import render_template, request, flash, redirect
from app import mongo
import datetime
import pymongo

@app.route('/')
def index():
    #client=mongo.connect()
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        register_package={
            'name':request.form['name'],
            'date':str(datetime.datetime.now()),
            'type':'user',
        }
        return str(register_package)

    else:
        return render_template("login.html")