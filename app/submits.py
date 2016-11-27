import requests, datetime, json
from app import database, user
from markdown2 import Markdown


class BaseSubmit():
    def execute(self):
        pass
    
    def construct_payload(self):
        return self.__dict__

    def acquire_time(self):
        return datetime.datetime.strftime(datetime.datetime.utcnow(),"%a, %d %b %Y %H:%M:%S GMT")

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
        self.username = ArticlePackage["username"]
        self.content=ArticlePackage["content"]
        self.submit_time=self.acquire_time()
        self.title=ArticlePackage["title"]
        self.categories=ArticlePackage["categories"]
    
    def execute(self):
        collection="articles"
        return database.insert(collection,self.construct_payload())