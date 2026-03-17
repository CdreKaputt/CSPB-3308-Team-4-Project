from flask import Blueprint, render_template, session, redirect, url_for
from app.auth import required_logged_in

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    if session.get("user"):
        return redirect(url_for("main.dashboard"))
    return redirect(url_for("auth.login"))


@main_bp.route("/dashboard")
@required_logged_in
def dashboard():
    # TODO: fetch trips associated with session["user"] via Trips model
    dummy_trips = [
        {
            "name": "Big Bend Rafting Trip",
            "departure_date": "Apr 15, 2026",
            "party_size": 12,
            "id": 2,
        },
        {
            "name": "Star Gazing Weekend: Shelf Road",
            "departure_date": "May 22, 2026",
            "party_size": 4,
            "id": 3,
        },
        {
            "name": "Tour of the Moon",
            "departure_date": "Sept 14, 2026",
            "party_size": 2,
            "id": 4,
        },
        {
            "name": "Lake Tahoe Ski Trip",
            "departure_date": "Dec 15, 2026",
            "party_size": 8,
            "id": 1,
        },
    ]
    return render_template("dashboard.html", trips=dummy_trips)


@main_bp.route("/about")
def about():
    return render_template("about.html")
