from functools import wraps
from flask import abort
from flask_jwt_extended import JWTManager, get_jwt_identity, verify_jwt_in_request

def jwt_required_with_role(the_role):
    def check(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            identity = get_jwt_identity()
            if identity['role'] not in the_role:
                abort(403, 'Admins only')
                # return {"msg": 'Admins only!'}
                # return jsonify(msg='Admins only!'), 403
            else:
                return fn(*args, **kwargs)
        return wrapper
    return check