from flask import Blueprint, render_template, session, redirect, url_for
from app.utils.auth import required_logged_in
from app.models.membership import Membership

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
