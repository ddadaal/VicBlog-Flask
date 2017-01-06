import requests, json
from app import database, user
from markdown2 import Markdown
from flask import Markup
from datetime import datetime


class BaseSubmit():
    def execute(self):
        pass
    
    def construct_payload(self):
        return self.__dict__

    def acquire_time(self):
        return datetime.now().timestamp()

class RegisterSubmit(BaseSubmit):
    def __init__(self, RegisterPackage):
        self.username=RegisterPackage["username"]
        self.password=RegisterPackage['password']
        self.role="user"
        self.register_time=self.acquire_time()
    
    def exist(self):
        query={"username":self.username}
        return database.find_one("users",query)!=None

    def execute(self):
        payload=self.construct_payload()
        if self.exist():
            return "Existing"
        else:
            database.insert("users",payload)
            return "OK"

class LoginSubmit(BaseSubmit):
    def __init__(self, LoginPackage):
        self.username=LoginPackage["username"]
        self.password=LoginPackage["password"]
        self.role=LoginPackage["role"]
    
    def validate_login(self):
        query={"username":self.username}
        document=database.find_one("users",query)
        if document['password']==self.password:
            return True, document
        else:
            return False, None

    def execute(self):
        status, document=self.validate_login()
        if status:
            return 200, user.generate(document["username"],document["role"])
        else:
            return 401, ""

class ArticleSubmit(BaseSubmit):
    def __init__(self, ArticlePackage:dict):
        self.collection="articles"
        self.username = ArticlePackage["username"]
        self.content=ArticlePackage["content"]
        self.submit_time=self.acquire_time()
        self.title=ArticlePackage["title"]
        self.categories=ArticlePackage["categories"]
        self.id=str(database.count("articles"))

    def execute(self):
        return database.insert(self.collection,self.construct_payload())
    

def format_article(article):
    formated =article
    markdownor=Markdown()
    formated["content"] = Markup(markdownor.convert(article["content"]))
    formated["submit_time"]=datetime.fromtimestamp(article["submit_time"]).strftime("%B %d, %Y")
    del formated["_id"]
    return formated