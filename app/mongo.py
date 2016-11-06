import pymongo

def connect():
    client=pymongo.MongoClient()
    return client