from flask import Flask
from eve import Eve

app=Flask(__name__)

from app import views