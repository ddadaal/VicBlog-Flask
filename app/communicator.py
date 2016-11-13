import requests

address="http://127.0.0.1:5001/users"

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
