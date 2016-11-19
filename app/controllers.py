from app import app,database,user
from flask import Markup, g, request

def acquire_articles():
    articles=[]
    for article in database.find("articles",None):
        articles.append({
            "username":article["username"],  
            "content":Markup(article["content"]),
            "submit_time":article["submit_time"],
            "title":article["title"], 
        })
    return articles

def check_login():
    token=request.cookies.get("login")
    current_user = user.User.create_from_token(token)
    g.user = current_user