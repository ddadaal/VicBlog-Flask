import datetime,base64,hmac

class Token():
    def __init__(self,username):
        self.username=username
        self.activated_time=datetime.datetime.utcnow()

    def __str__(self):
        ts=datetime.datetime.timestamp(datetime.datetime.utcnow())
        return self.username+"_"+str(ts)
    
    def generate_token(self):
        header={
            "alg":"HS256", 
            "typ":"JWT", 
        }
        payload={
            "username": self.username, 
        }

        header=base64.urlsafe_b64encode(str(header).encode())
        payload=base64.urlsafe_b64encode(str(payload).encode())

        h=hmac.new(b"233233233","{0}.{1}".format(header,payload).encode())
        signature=base64.urlsafe_b64encode(h.digest())

        return "{0}.{1}.{2}".format(str(header),str(payload),str(signature))
