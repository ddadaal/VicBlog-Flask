import app,jwt

secret="233333333333333333"

def generate(username):
    return jwt.encode({"username":username}, secret, algorithm='HS256')

def decode(token):
    return jwt.decode(token,secret,algorithms=['HS256'])


class User():
    def __init__(self):
        self.username=""

    def create_from_token(token):
        if not is_logged_in(token):
            return None
        user=User()
        user.username = decode(token)['username']
        return user
    
def is_logged_in(token):
    try:
        decode(token)
    except:
        return False
    return True