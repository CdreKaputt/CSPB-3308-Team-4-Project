from functools import wraps
from flask import abort, session, flash, redirect, url_for, request
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

def required_logged_out(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # check if the 'user' key exists in session
        if "user" in session:
            flash("You must be logged out to access that page.", "error")
            return(redirect(url_for("main.home")))
        else:
        # otherwise user is logged out, grant access (signup/login only)
            return f(*args, **kwargs)
    
    return decorated

def required_logged_in(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if the 'user' key exits in session
        if "user" not in session:
            flash("You must be logged in to access that page.", "error")
            return redirect(url_for("auth_forms.login"))

        # Otherwise user must be logged in, grant access
        return f(*args, **kwargs)

    return decorated
    