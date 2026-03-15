from flask import Blueprint, render_template, session
from app.middleware.auth import required_logged_in


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/dashboard")
@required_logged_in
def dashboard():
    
    # need to fetch trips associated with session["user"]
    dummy_trips = [
        {
            "name": "Lake Tahoe Ski Trip",
            "departure_date": "Dec 15, 2026",
            "party_size": 8,
            "id": 1
        },
        {
            "name": "Austin Bachelor Party",
            "departure_date": "Jan 22, 2027",
            "party_size": 12,
            "id": 2
        },
        {
            "name": "Quick Getaway: Sedona",
            "departure_date": "Feb 05, 2027",
            "party_size": 4,
            "id": 3
        },
        {
            "name": "Japan Cherry Blossom Tour",
            "departure_date": "Mar 28, 2027",
            "party_size": 2,
            "id": 4
        }
    ]
    
    return render_template("dashboard.html", trips=dummy_trips)

@main_bp.route("/about")
def about():
    return render_template("about.html")