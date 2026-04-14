from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.utils.auth import required_logged_in
from app.extensions import db
from app.models import Item, Trip

items_bp = Blueprint("items", __name__)


@items_bp.route("/<int:trip_id>", methods=["GET"])
@required_logged_in
def packlist(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    return render_template("packlist.html", trip=trip, items=trip.items)


@items_bp.route("/new", methods=["GET", "POST"])
@required_logged_in
def new_item():
    user = session.get("user")

    if request.method == "GET":
        trip_id = request.args.get("trip_id", type=int)
        trip = Trip.query.get_or_404(trip_id)
        return render_template("new_item_form.html", trip=trip)

    # if "POST"
    trip_id = request.form.get("trip_id", type=int)
    trip = Trip.query.get_or_404(trip_id)

    item = Item(
        trip_id=trip_id,
        name=request.form.get("name"),
        description=request.form.get("description"),
        category=request.form.get("category"),
        quantity=request.form.get("quantity", 1, type=int),
        user_id=user["id"],
        created_by=user["id"],
    )
    try:
        db.session.add(item)
        db.session.commit()
        flash("Item added!")
        return redirect(url_for("items.packlist", trip_id=trip_id))
    except Exception:
        db.session.rollback()
        flash("Could not add item. Please try again.", "error")
        return render_template("new_item_form.html", trip=trip)


@items_bp.route("/<int:item_id>/edit", methods=["GET", "POST"])
@required_logged_in
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)

    if request.method == "GET":
        trip = Trip.query.get_or_404(item.trip_id)
        return render_template("edit_item_form.html", item=item, trip=trip)

    # if "POST"
    item.name = request.form.get("name")
    item.description = request.form.get("description")
    item.category = request.form.get("category")
    item.quantity = request.form.get("quantity", item.quantity, type=int)
    item.is_completed = bool(request.form.get("is_completed"))

    try:
        db.session.commit()
        flash("Item updated!")
        return redirect(url_for("items.packlist", trip_id=item.trip_id))
    except Exception:
        db.session.rollback()
        flash("Could not update item. Please try again.", "error")
        trip = Trip.query.get_or_404(item.trip_id)
        return render_template("edit_item_form.html", item=item, trip=trip)


@items_bp.route("/<int:item_id>/delete", methods=["POST"])
@required_logged_in
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    trip_id = item.trip_id
    try:
        db.session.delete(item)
        db.session.commit()
        flash("Item removed!")
        return redirect(url_for("items.packlist", trip_id=trip_id))
    except Exception:
        db.session.rollback()
        flash("Could not remove item. Please try again.", "error")
        return redirect(url_for("items.packlist", trip_id=trip_id))
