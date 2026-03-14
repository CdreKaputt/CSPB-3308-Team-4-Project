from flask import Blueprint, render_template
from app.middleware.auth import required_logged_in


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/dashboard")
@required_logged_in
def dashboard():
    return render_template("dashboard.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")