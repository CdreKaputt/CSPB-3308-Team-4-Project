from functools import wraps
from flask import session, flash, redirect, url_for


def required_logged_in(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if the 'user' key exists in session
        if "user" not in session:
            flash("You must be logged in to access that page.", "error")
            return redirect(url_for("auth.login"))
        # Otherwise user must be logged in, grant access
        return f(*args, **kwargs)

    return decorated


def required_logged_out(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if the 'user' key exists in session
        if "user" in session:
            flash("You must be logged out to access that page.", "error")
            return redirect(url_for("main.home"))
        # Otherwise user is logged out, grant access (signup/login only)
        return f(*args, **kwargs)

    return decorated
