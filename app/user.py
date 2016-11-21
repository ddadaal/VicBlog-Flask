import app
from jose import jwt

secret="hhh233333333333333333"

def generate(username):
    return jwt.encode({"username":username}, secret, algorithm='HS256')

def decode(token):
    return jwt.decode(token,secret,algorithms=['HS256'])


class User():
    def __init__(self):
        self.username=""

    def create_from_token(token):
        user=User()
        try:
            user.username = decode(token)['username']
        except:
            return None
        return user