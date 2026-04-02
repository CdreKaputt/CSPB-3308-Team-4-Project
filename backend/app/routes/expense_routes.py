from flask import Blueprint, render_template, redirect, url_for, flash, session, request, abort
from app.extensions import db
from app.models import Expense, Trip, User
from decimal import Decimal


expenses_bp = Blueprint("expenses", __name__)

# return expense list for a given trip_id
@expenses_bp.route('/<int:trip_id>', methods=['GET'])
def trip_expenses(trip_id):
    
    # make sure trip exists
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)
    
    expenses = trip.expenses
    total = 0
    for exp in expenses:
        total += exp.amount
        
    # passing trip to expense index because we can use trip.expenses association
    return render_template('expenses_index.html', trip=trip, expenses=expenses, total=total)

@expenses_bp.route("/<int:trip_id>/new", methods=['GET', 'POST'])
def new_expense(trip_id):
    
    # make sure trip exists
    trip = db.session.get(Trip, trip_id)
    if not trip:
        abort(404)
    
    if request.method == "POST":
        description = request.form.get("description")
        amount_str = request.form.get("amount")
        payer_id = request.form.get("payer_id")
        is_paid = request.form.get("is_paid")
        
        # make sure amount is Decimal not string
        amount = Decimal(amount_str)
        
        new_exp = Expense(
            trip_id=trip_id,
            payer_id=int(payer_id),
            amount=amount,
            description=description,
            is_paid=bool(is_paid)
        )
        db.session.add(new_exp)
        db.session.commit()
        

        
        return redirect(url_for("expenses.trip_expenses", trip_id=trip_id))
        
    return render_template("new_expense_form.html", trip=trip)

@expenses_bp.route('/edit/<int:expense_id>', methods=['GET', 'POST'])
def edit_expense(expense_id):
    
    expense = db.session.get(Expense, expense_id)
    if not expense:
        abort(404)
        
    if request.method == 'POST':
        expense.description = request.form.get("description")
        expense.amount = Decimal(request.form.get("amount"))
        expense.payer_id = int(request.form.get("payer_id"))
    
        # check value of checkbox for is_paid
        expense.is_paid = True if request.form.get('is_paid') else False
        
        db.session.commit()

        return redirect(url_for('expenses.trip_expenses', trip_id=expense.trip_id))

    trip = db.session.get(Trip, expense.trip_id)
    return render_template('edit_expense_form.html', expense=expense, trip=trip)