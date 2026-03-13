from functools import wraps
from flask import abort
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def guest_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        verified = False
        try:
            verify_jwt_in_request(optional=True)
            verified = True
        except Exception:
            pass
        if verified and get_jwt_identity():
            abort(403)
        return f(*args, **kwargs)
    return decorated