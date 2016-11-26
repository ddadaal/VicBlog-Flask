from flask import Flask, url_for
app=Flask(__name__)

upload_path = "app/static/upload"
app.config['UPLOAD_FOLDER'] = upload_path
app.config['ALLOWED_EXTENSIONS']=('txt','jpg')

from app import views