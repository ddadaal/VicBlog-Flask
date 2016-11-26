from flask import Flask
app=Flask(__name__)

upload_path="static/upload/"
app.config['UPLOAD_FOLDER'] = upload_path
from app import views