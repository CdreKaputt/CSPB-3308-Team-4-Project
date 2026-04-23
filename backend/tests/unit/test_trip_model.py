from app.models import Trip
from datetime import date

def test_new_trip():
    trip = Trip(
        trip_name="Test Trip 2026",
        leader_id=1,
        start_date=date(2026, 4, 1),
        end_date=date(2026, 4, 7),
        public=False,
    )
    assert trip.trip_name == "Test Trip 2026"
    assert trip.leader_id == 1
    assert trip.start_date == date(2026, 4, 1)
    assert trip.end_date == date(2026, 4, 7)
    assert trip.__repr__() == "<Trip Test Trip 2026>"