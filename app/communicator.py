import requests, datetime, json

address="http://127.0.0.1:5001/users"

class Token():
    def __init__(self,username):
        self.username=username
        self.activated_time=datetime.datetime.utcnow()

    def __str__(self):
        ts=datetime.datetime.timestamp(datetime.datetime.utcnow())
        return self.username+"_"+str(ts)

class BaseSubmit(object):
    submit_url=None

    def execute(self):
        pass
    
    def construct_payload(self):
        pass

    def acquire_time(self):
        return datetime.datetime.strftime(datetime.datetime.utcnow(),"%a, %d %b %Y %H:%M:%S GMT")

class LoginSubmit(BaseSubmit):
    def __init__(self, LoginPackage):
        self.username=LoginPackage["username"]
        self.password=LoginPackage["password"]
        self.role=LoginPackage["role"]
        self.submit_url="http://127.0.0.1:5001/session"
    
    def construct_payload(self):
        payload={
            'username':self.username, 
            'password':self.password,
            'role':"user", 
            'time':self.acquire_time(), 
        }
        return payload
    
    def validate_login(self):
        user_url="http://127.0.0.1:5001/users/"+self.username
        response=json.loads(requests.get(user_url).text)
        return response["password"]==self.password


    def execute(self):
        payload=self.construct_payload()
        if self.validate_login():
            token=Token(self.username)
            return str(token)
        else:
            return "Wrong Password!"

class RegisterSubmit(BaseSubmit):
    def __init__(self, RegisterPackage):
        self.username=RegisterPackage['username']
        self.password=RegisterPackage['password']
        self.role=RegisterPackage["role"]
        self.submit_url="http://127.0.0.1:5001/users"
    
    def construct_payload(self):
        payload={
            'username':self.username, 
            'password':self.password,
            'role':"user", 
            'time':self.acquire_time(), 
        }
        return payload

    def execute(self):
        payload=self.construct_payload()
        if not self.check():
            return "User existing. Change the username "
        else:
            return requests.post(self.submit_url,payload).text
    
    def check(self):
        url=self.submit_url+"/"+self.username
        return requests.get(url).status_code==404


def add(package,update_if_exists=True):
    if not exists(package):
        return requests.post(address,data=package)
    else:
        return update(package)

def exists(package):
    name=package['name']
    response=requests.get(address+"/"+name)
    return response.status_code!=404

def update(package):
    name=package["name"]
    full_path=address+"/"+name
    return requests.patch(full_path,data=package)
