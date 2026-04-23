from app.models import Expense
from datetime import datetime


def test_new_trip():
    expense= Expense(
        trip_id=1,
        payer_id=1,
        amount=2.50,
        description="Some test item",
        is_paid=False
    )
    assert expense.trip_id == 1
    assert expense.payer_id == 1
    assert expense.amount == 2.50
    assert expense.description == "Some test item"
    assert expense.is_paid == False
    assert isinstance(expense.created_at, datetime)
    assert isinstance(expense.updated_at, datetime)
    assert expense.__repr__() == f"<Expense {expense.id}>"