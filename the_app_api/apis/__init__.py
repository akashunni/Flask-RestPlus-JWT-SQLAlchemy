from flask_restplus import Api

from the_app_api.apis.test import namespace as ns_test
from the_app_api.apis.user import namespace as ns_user

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(title='Test API', version=1, description='The Test API description.', authorizations=authorizations)

api.add_namespace(ns_user)
api.add_namespace(ns_test)