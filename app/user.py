import app

class User():
    def __init__(self):
        self.username=""

    def create_from_token(token):
        if token=="" or token==None:
            return None
        user=User()
        user.username = app.token.decode(token)['username']
        return user