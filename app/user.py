import app,json
from jose import jwt

secret="hhh233333333333333333"

def generate(username:str,role:str) -> str:
    return jwt.encode({"username":username,"role":role}, secret, algorithm='HS256')

def decode(token:str) -> dict:
    return jwt.decode(token,secret,algorithms=['HS256'])


class User():
    def __init__(self):
        self.username=""
        self.role=""

    def create_from_token(token):
        user=User()
        try:
            package=decode(token)
            user.username=package["username"]
            user.role=package['role']
        except:
            return None
        return user
    
    def generate_token(self):
        return generate(self.username,self.role)

    
class UserEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,User):
            return obj.__dict__
        return json.JSONEncoder.default(self,obj)

