from app.models import Item

def test_new_item():
    item = Item(
        trip_id=1,
        name="Test Item",
        user_id=1,
        created_by=1,
        description="A test item description",
        category="Test Category",
        quantity=2,
    )
    assert item.trip_id == 1
    assert item.name == "Test Item"
    assert item.user_id == 1
    assert item.created_by == 1
    assert item.description == "A test item description"
    assert item.category == "Test Category"
    assert item.quantity == 2
    assert item.is_completed == False
    assert item.status == "active"
    assert item.__repr__() == "<Item: Test Item"


def test_new_item_defaults():
    item = Item(
        trip_id=1,
        name="Minimal Item",
        user_id=1,
        created_by=1,
    )
    assert item.quantity == 1
    assert item.is_completed == False
    assert item.status == "active"
    assert item.description is None
    assert item.category is None