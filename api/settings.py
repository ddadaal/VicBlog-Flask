MONGO_HOST='localhost'
MONGO_PORT=27017

MONGO_DBNAME='vicblog'



RESOURCE_METHODS=['GET','POST','DELETE']
ITEM_METHODS=['GET','PATCH','PUT','DELETE']

schema={
    'name':{
        'type':"string",
        'minlength':1,
    },
    'role':{
        'type':'string',
        'allowed':['user','admin'],
    },
    'sign_up_time':{
        'type':'datetime',
    }
}

user={
    'additional_lookup':{
        'url':'regex("[\w]+")',
        'field':'name'
    },
    'resource_methods':['GET','POST'],
    'schema':schema,
}

DOMAIN={'user':user}