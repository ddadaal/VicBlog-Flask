import requests

address="http://127.0.0.1:5001/user"

def add(package):
    return requests.post(address,data=package).text