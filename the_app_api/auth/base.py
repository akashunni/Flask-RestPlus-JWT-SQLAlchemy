from functools import wraps
from flask import abort
from flask_jwt_extended import JWTManager, get_jwt_identity, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError

def jwt_required_with_role(the_role):
    def check(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except NoAuthorizationError:
                abort(401, 'Missing Authorization Header')
            identity = get_jwt_identity()
            if identity['role'] not in the_role:
                abort(403, 'Permission Denied for ' + identity['role'])
            else:
                return fn(*args, **kwargs)
        return wrapper
    return check