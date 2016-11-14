import requests,datetime

address="http://127.0.0.1:5001/users"

class BaseSubmit(object):
    submit_url=None

    def execute(self):
        pass
    
    def construct_payload(self):
        pass

    def acquire_time(self):
        return datetime.datetime.strftime(datetime.utcnow(),"%a, %d %b %Y %H:%M:%S GMT")

class LoginSubmit(BaseSubmit):
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.submit_url="http://127.0.0.1:5001/users"
    
    def construct_payload(self):
        payload={
            'username':self.username, 
            'password':self.password, 
            'time':self.acquire_time(), 
        }
        return payload
    
    def execute(self):
        payload=self.construct_payload()
        response=requests.get(self.submit_url, payload)



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
