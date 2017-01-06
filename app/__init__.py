from flask import Flask, url_for
from flask_cors import CORS, cross_origin
app=Flask(__name__)
CORS(app)

upload_path = "app/static/upload"
app.config['UPLOAD_FOLDER'] = upload_path
app.config['ALLOWED_EXTENSIONS']=('txt','jpg')

from app import views