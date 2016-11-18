import jwt
secret="233333333333333333"

def generate(username):
    return jwt.encode({"username":username}, secret, algorithm='HS256')

def decode(token):
    return jwt.decode(token,secret,algorithms=['HS256'])
