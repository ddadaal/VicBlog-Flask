MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'vicblog'


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema_user = {
    'name': {
        'type': "string",
        'minlength': 1,
    },
    'role': {
        'type': 'string',
        'allowed': ['user', 'admin'],
    },
    'sign_up_time': {
        'type': 'datetime',
    }
}

user = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    'resource_methods': ['GET', 'POST','PATCH'],
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

DOMAIN = {'users': user,'article': article}
