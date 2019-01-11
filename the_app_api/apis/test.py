from flask_restplus import Namespace, fields, Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from the_app_api.auth.base import jwt_required_with_role

namespace = Namespace('test', description='Just a test endpoint.')

test_schema = namespace.model('Test', {
    'test_id': fields.Integer(description='The ID', required=True),
    'test_name': fields.String(description='The name', reqiured=True),
    'test_key': fields.String(description='The Key', required=True)
})

@namespace.route('/')
class Test(Resource):
    
    @namespace.marshal_with(test_schema)
    @namespace.doc('Just a GET endpoint.')
    @namespace.doc(security='apikey')
    @jwt_required_with_role(['admin', 'enduser'])
    def get(self):
        return {
            'test_id': 1,
            'test_name': 'Akash',
            'test_key': 'e245jba38yhq2rh912',
            'junk_key': 'faffffff'
        }
    
    @namespace.expect(test_schema, validate=True)
    @namespace.marshal_with(test_schema)
    @namespace.doc('Just a POST endpoint.')
    def post(self):
        print("came")
        return self.data_parser()
    
    @staticmethod
    def data_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('test_id', type=int)
        parser.add_argument('test_name', type=str)
        parser.add_argument('test_key', type=str)
        return parser.parse_args()
