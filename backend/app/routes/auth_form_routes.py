from flask import Blueprint, render_template
from app.middleware.auth import required_logged_out

auth_forms_bp = Blueprint('auth_forms', __name__)

@auth_forms_bp.route("/login", methods=["GET"])
@required_logged_out
def login():
    return render_template("login.html")

@auth_forms_bp.route("/signup", methods=["GET"])
@required_logged_out
def signup():  
    return render_template("signup.html")
