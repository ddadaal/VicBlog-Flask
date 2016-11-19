import requests, datetime, json
from app import database, token, user
from markdown2 import Markdown

address="http://127.0.0.1:5001/users"


class BaseSubmit(object):
    submit_url=None

    def execute(self):
        pass
    
    def construct_payload(self):
        pass

    def acquire_time(self):
        return datetime.datetime.strftime(datetime.datetime.utcnow(),"%a, %d %b %Y %H:%M:%S GMT")

class RegisterSubmit(BaseSubmit):
    def __init__(self, RegisterPackage):
        self.username=RegisterPackage["username"]
        self.password=RegisterPackage['password']
        self.role="user"

    def construct_payload(self):
        payload={
            'username':self.username, 
            'password':self.password,
            'register_time':self.acquire_time(),
            'role':self.role, 
        }
        return payload
    
    def exist(self):
        query={"username":self.username}
        return database.find_one("users",query)!=None

    def execute(self):
        payload=self.construct_payload()
        if self.exist():
            return "Existing"
        else:
            return str(database.insert("users",payload))

class LoginSubmit(BaseSubmit):
    def __init__(self, LoginPackage):
        self.username=LoginPackage["username"]
        self.password=LoginPackage["password"]
        self.role=LoginPackage["role"]
    
    def validate_login(self):
        query={"username":self.username}
        return database.find_one("users",query)['password']==self.password


    def execute(self):
        if self.validate_login():
            return 200, token.generate(self.username)
        else:
            return 402, ""

class ArticleSubmit(BaseSubmit):
    def __init__(self, ArticlePackage):
        self.user = ArticlePackage.user
        self.content=ArticlePackage.content
        self.submit_time=self.acquire_time()
        self.title=ArticlePackage.title

    def construct_payload(self):
        payload={
            "username": self.user.username,
            "submit_time": self.submit_time, 
            "content": self.content,
            "title": self.title,  
        }
        return payload
    
    def execute(self):
        collection="article"
        return database.insert(collection,self.construct_payload())

# class RegisterSubmit(BaseSubmit):
#     def __init__(self, RegisterPackage):
#         self.username=RegisterPackage['username']
#         self.password=RegisterPackage['password']
#         self.role=RegisterPackage["role"]
#         self.submit_url="http://127.0.0.1:5001/users"
    
#     def construct_payload(self):
#         payload={
#             'username':self.username, 
#             'password':self.password,
#             'role':"user", 
#             'time':self.acquire_time(), 
#         }
#         return payload

#     def execute(self):
#         payload=self.construct_payload()
#         if not self.exist():
#             return "User existing. Change the username "
#         else:
#             return requests.post(self.submit_url,payload).text
    
#     def exist(self):
#         url=self.submit_url+"/"+self.username
#         return requests.get(url).status_code==404