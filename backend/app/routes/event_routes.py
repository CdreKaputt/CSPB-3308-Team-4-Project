from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.utils.auth import required_logged_in
from app.extensions import db
from app.models import Events, Trip
from datetime import datetime

events_bp = Blueprint("events", __name__)

# events index
@events_bp.route('/<int:trip_id>', methods=['GET'])
@required_logged_in
def trip_events(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    events = Events.query.filter_by(trip_id=trip_id).order_by(Events.event_date).all()
    return render_template("events_index.html", events=events, trip=trip)

# new event
@events_bp.route("/<int:trip_id>/new", methods=["GET", "POST"])
@required_logged_in
def new_event_form(trip_id):
    user = session.get('user')
    trip = Trip.query.get_or_404(trip_id)
    if request.method == "GET":
        return render_template("new_event_form.html", trip=trip, user=user)


    if request.method == "POST":
        event_name = request.form.get("event_name")
        description = request.form.get("description")
        event_date = request.form.get("event_date")
        event = Events(
                event_name=event_name,
                description=description,
                event_date=datetime.strptime(event_date, '%Y-%m-%d').date(),
                owner_id=user['id'],
                trip_id=trip_id
            )
        try:
            db.session.add(event)
            db.session.commit()
            flash("Event created!")
            return redirect(url_for("events.trip_events", trip_id=trip_id))
        except Exception:
            # Roll back any partial changes if the database write fails
            db.session.rollback()
            flash("Could not create event. Please try again.", "error")
            return render_template("new_event_form.html", trip=trip, user=user)

# event overview
@events_bp.route("/<int:event_id>/")
@required_logged_in
def event_overview(event_id):
    event = Events.query.get_or_404(event_id)
    return render_template("event_overview.html", event=event)

# edit event
@events_bp.route("/edit/<int:event_id>", methods=["GET", "POST"])
@required_logged_in
def edit_event_form(event_id):
    event = Events.query.get_or_404(event_id)
    user = session.get('user')
    if request.method == "GET":
        return render_template("edit_event_form.html", event=event, user=user)
    if request.method == "POST":
        event.event_name = request.form.get("event_name")
        event.description = request.form.get("description")
        event.event_date = datetime.strptime(request.form.get("event_date"), '%Y-%m-%d').date()
        trip_id = event.trip_id
        try:
            db.session.commit()
            flash("Event updated!")
            return redirect(url_for("events.trip_events", trip_id=trip_id))
        except Exception:
            # Roll back any partial changes if the database write fails
            db.session.rollback()
            flash("Could not create event. Please try again.", "error")
            return render_template("edit_event_form.html", event=event, trip_id=trip_id, user=user)

# delete event
@events_bp.route("/delete/<int:event_id>", methods=["POST"])
@required_logged_in
def event_delete(event_id):
    event = Events.query.get_or_404(event_id)
    trip_id = event.trip_id
    try:
        db.session.delete(event)
        db.session.commit()
        flash("Event deleted!")
        return redirect(url_for("events.trip_events", trip_id=trip_id))
    except Exception:
        # Roll back any partial changes if the database write fails
        db.session.rollback()
        flash("Could not delete event. Please try again.", "error")
        return redirect(url_for("events.trip_events", trip_id=trip_id))