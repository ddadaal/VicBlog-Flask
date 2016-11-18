MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'vicblog'


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema_user = {
    'username': {
        'type': "string",
        'minlength': 1,
    }, 
    'password':{
        'type':'string', 
        'minlength': 1, 
    }, 
    'role':{
        'type':'string',
        'allowed':['user','admin'], 
    }, 
    'time': {
        'type': 'datetime',
    }, 
}

user = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': schema_user,
}

schema_article = {
    'author': {
        'type': 'string',
        'minlength': 1,
    },
    'publish_time': {
        'type': 'datetime',
    },
    'last_updated_time': {
        'type': 'datetime',
    },
    'ID': {
        'type': 'integer', 
    },
    'content': {
        'type': 'string',
        'minlength': 1,
    }, 
}

article = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'ID'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': schema_article,
}

login_attempt = {
    'resource_methods':['GET'], 
    'schema':schema_user, 
}


DOMAIN = {'users': user,'article': article, 'session': login_attempt}
