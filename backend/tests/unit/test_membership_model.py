from app.models import Membership

def test_new_membership():
    membership = Membership(
        trip_id=1,
        member_id=1,
    )
    assert membership.trip_id == 1
    assert membership.member_id == 1
    assert membership.__repr__() == f"<Membership {membership.id}>"