from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from the_app_api.apis import api
from the_app_api.resources.base import db
# from the_app_api.auth.base import jwt

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jabfniaw37yr9gfdaq'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///core/db_files/test.db'
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    # jwt.init_app(app)
    db.init_app(app)
    Migrate(app, db)
    api.init_app(app)
    return app

app = create_app()
# db = SQLAlchemy(app)
Migrate(app, db)
jwt = JWTManager(app)

# @jwt.user_claims_loader
# def add_role_field_to_token(user):
#     return {'role': user['role']}


if __name__ == "__main__":
    app.run(debug=True)