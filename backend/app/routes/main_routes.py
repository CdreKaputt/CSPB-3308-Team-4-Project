from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.auth import required_logged_in
from app.models.membership import Membership
from app.models.trip import Trip
from app import db

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    if session.get("user"):
        return redirect(url_for("main.dashboard"))
    return redirect(url_for("auth.login"))


@main_bp.route("/dashboard")
@required_logged_in
def dashboard():
    
    user_id = session['user']['id']
    memberships = Membership.query.filter_by(member_id=user_id).all()
    
    trips = []
    
    for m in memberships:
        trip = m.trip
        trips.append(trip)
        print(trip.id)

    return render_template("dashboard.html", trips=trips)


@main_bp.route("/about")
def about():
    return render_template("about.html")


@main_bp.route("/discover")
def discover():
    # public_trips = db.session.query(Trip).filter_by(public=True).all()
    public_trips = Trip.query.filter_by(public = True ).all()
    return render_template("discover.html", trips=public_trips)