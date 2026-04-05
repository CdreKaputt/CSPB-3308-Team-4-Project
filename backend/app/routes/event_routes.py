from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.utils.auth import required_logged_in
from app.extensions import db
from app.models import Events

main_bp = Blueprint("events", __name__)

# events index
@main_bp.route("/<int:trip_id>/events")
@required_logged_in
def trip_events(trip_id):
    events = Events.query.filter_by(trip_id=trip_id).all()
    return render_template("events_index.html", events=events, trip_id=trip_id)

# new event
@main_bp.route("/<int:trip_id>/new_event", methods=["GET", "POST"])
@required_logged_in
def new_event_form(trip_id):
    if request.method == "GET":
        return render_template("new_event_form.html", trip_id=trip_id)

    if request.method == "POST":
        event_name = request.form.get("event_name")
        description = request.form.get("description")
        event_date = request.form.get("event_date")
        user_id = request.form.get("user_id")
        event = Events(
                event_name=event_name,
                description=description,
                event_date=event_date,
                owner_id=user_id,
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
            return render_template("new_event_form.html", trip_id=trip_id)

# event overview
@main_bp.route("/<int:event_id>/event_overview")
@required_logged_in
def event_overview(event_id):
    event = Events.query.get_or_404(event_id)
    return render_template("events_overview.html", event=event)

# edit event
@main_bp.route("/<int:event_id>/edit_event", methods=["GET", "POST"])
@required_logged_in
def edit_event_form(event_id):
    event = Events.query.get_or_404(event_id)
    if request.method == "GET":
        return render_template("edit_event.html", event=event)
    if request.method == "POST":
        event.event_name = request.form.get("event_name")
        event.description = request.form.get("description")
        event.event_date = request.form.get("event_date")
        trip_id = event.trip_id
        try:
            db.session.commit()
            flash("Event updated!")
            return redirect(url_for("events.trip_events", trip_id=trip_id))
        except Exception:
            # Roll back any partial changes if the database write fails
            db.session.rollback()
            flash("Could not create event. Please try again.", "error")
            return render_template("edit_event.html", event=event, trip_id=trip_id)

# delete event
@main_bp.route("/<int:event_id>/delete", methods=["POST"])
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