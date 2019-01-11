from flask import jsonify
from flask_restplus import Namespace, fields, Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, set_access_cookies
from the_app_api.resources.base import db
from the_app_api.resources.models import User


namespace = Namespace('user', description='User things.')

user_login_schema = namespace.model('User', {
    'username': fields.String(description='The username', reqiured=True),
    'password': fields.String(description='The password', required=True)
})

@namespace.route('/login')
class Test(Resource):
    @namespace.expect(user_login_schema)
    @namespace.doc('Just a GET endpoint.')
    def post(self):
        response = self.data_parser()
        username = response.username
        password = response.password
        
        user = User.query.filter_by(username=username).first()

        if user is None:
            return {"Error": "No such user exists."}
        elif user.password == password:
            resp = jsonify({'login': True})
            set_access_cookies(resp, create_access_token(identity={"username": user.username, "role": user.role}))
            return resp
            # return create_access_token(identity={"username": user.username, "role": user.role})
        else:
            return {"Error": "Wrong Password!"}
    
    @staticmethod
    def data_parser():
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        return parser.parse_args()
