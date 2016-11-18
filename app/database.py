import pymongo

url="localhost"
port=27017
db_name="vicblog"


def connect():
    connection=pymongo.MongoClient(url,port)
    return connection[db_name]

def insert(collection, payload):
    db=connect()
    return db[collection].insert_one(payload).inserted_id

def find_one(collection, query):
    db=connect()
    return db[collection].find_one(query)
