from app.models import Events
from datetime import datetime, date


def test_new_trip():
    event = Events(
        event_name="Some Event",
        description="Some event description",
        event_date=date(2026, 4, 1),
        owner_id=1,
        trip_id=1,
    )
    assert event.event_name == "Some Event"
    assert event.description == "Some event description"
    assert event.event_date == date(2026, 4, 1)
    assert event.owner_id == 1
    assert event.trip_id == 1
    assert isinstance(event.created_at, datetime)
    assert isinstance(event.updated_at, datetime)
    assert event.__repr__() == f"<Event {event.event_name}>"