from flask import Blueprint, render_template, redirect, url_for, flash, session, request, abort
from app.extensions import db
from app.models import Trip, User, Membership
from datetime import datetime, timedelta

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
    current_membership = None
    
    for membership in memberships:
        user = db.session.get(User, membership.member_id)
        if not user:
            continue
        members.append(user)
        if membership.member_id == session['user']['id']:
            current_membership = membership
    
    return render_template('trip_show.html', trip=trip, members=members, current_membership=current_membership)
    
@trips_bp.route("/new", methods=['GET', 'POST'])
def create_trip():
    if request.method == 'POST':
        # get trip data from form
        trip_name = request.form.get('trip_name')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        leader_id = request.form.get('leader_id')

        # create trip and add to db
        new_trip = Trip(
            trip_name=trip_name,
            start_date=datetime.strptime(start_date, '%Y-%m-%d'),
            end_date=datetime.strptime(end_date, '%Y-%m-%d'),
            leader_id=leader_id
        )
        
        db.session.add(new_trip)
        db.session.commit()
        
        # create membership
        new_membership = Membership(
            member_id=leader_id,
            trip_id=new_trip.id
        )
        
        db.session.add(new_membership)
        db.session.commit()
        return redirect(url_for('trips.trip_show', trip_id=new_trip.id))
        
    return render_template('new_trip_form.html')
        
        
@trips_bp.route("/<int:trip_id>/edit", methods=['GET', 'POST'])
def edit_trip(trip_id):
    
    # make sure trip exists
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)
        
    if request.method == 'POST': 
        # get trip data from form
        trip.trip_name = request.form.get('trip_name')
        trip.start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d')
        trip.end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d')
        
        db.session.commit()
        
        return redirect(url_for('trips.trip_show', trip_id=trip.id))
        
    return render_template('edit_trip_form.html', trip=trip)


@trips_bp.route('/delete/<int:trip_id>', methods=['POST'])
def delete_trip(trip_id):
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)
    
    db.session.delete(trip)
    db.session.commit()
    
    return redirect(url_for('main.dashboard'))


@trips_bp.route('/<int:trip_id>/memberships', methods=['POST'])
def add_member(trip_id):
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)

    if trip.leader_id != session['user']['id']:
        flash("Only the trip owner can add members.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    username = request.form.get('username', '').strip()
    if not username:
        flash("Please enter a username to add.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    user = User.query.filter_by(username=username).first()
    if not user:
        flash("No user found with that username.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    existing_membership = Membership.query.filter_by(
        trip_id=trip.id,
        member_id=user.id
    ).first()
    if existing_membership:
        flash("That user is already a member of this trip.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    db.session.add(Membership(trip_id=trip.id, member_id=user.id))
    db.session.commit()
    flash(f"{user.username} was added to the trip.", "success")
    return redirect(url_for('trips.trip_show', trip_id=trip.id))


@trips_bp.route('/memberships/delete/<int:membership_id>', methods=['POST'])
def delete_membership(membership_id):
    membership = db.session.get(Membership, membership_id)
    if not membership:
        abort(404)

    trip = db.session.get(Trip, membership.trip_id)
    if not trip:
        abort(404)

    if membership.member_id != session['user']['id']:
        flash("You can only remove yourself from a trip.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    if trip.leader_id == session['user']['id']:
        flash("Trip owners cannot remove themselves from their own trip.", "error")
        return redirect(url_for('trips.trip_show', trip_id=trip.id))

    db.session.delete(membership)
    db.session.commit()
    flash("You have been removed from the trip.", "success")
    return redirect(url_for('main.dashboard'))
