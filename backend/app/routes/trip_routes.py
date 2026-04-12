from flask import Blueprint, render_template, redirect, url_for, flash, session, request, abort
from app.extensions import db
from app.models import Trip, User

trips_bp = Blueprint("trips", __name__)

# get a trip for the trip show page
@trips_bp.route("/<int:trip_id>", methods=['GET'])
def trip_show(trip_id):
    
    # make sure trip exists
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)
        
    # get members
    memberships = trip.memberships
    members = []
    
    for membership in memberships:
        user = db.session.get(User, membership.member_id)
        members.append(user)
    
    return render_template('trip_show.html', trip=trip, members=members)
    
