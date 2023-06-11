from models import Passengers, passenger_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')

# Passenger helper functions
def read_all_passengers():
    passengers = Passengers.query.all()
    return passenger_schema.dump(passengers)

def create_passenger(passenger):
    id = passenger.get("id")
    existing_passenger = Passengers.query.filter(Passengers.id == id).one_or_none()

    if existing_passenger is None:
        new_passenger = passenger_schema.load(passenger, session=db.session)
        db.session.add(new_passenger)
        db.session.commit()
        return passenger_schema.dump(new_passenger), 201
    else:
        abort(
            406,
            f"Passenger with id {id} already exists",
        )

def update_passenger(id, passenger):
    update_passenger = Passengers.query.filter(Passengers.id == id).one_or_none()

    if update_passenger is not None:
        schema = passenger_schema.load(passenger, session=db.session)
        for key, value in schema.items():
            setattr(update_passenger, key, value)

        db.session.add(update_passenger)
        db.session.commit()

        data = passenger_schema.dump(update_passenger)

        return data, 200

    else:
        abort(
            404,
            f"Passenger not found for Id: {id}",
        )

def delete_passenger(id):
    passenger = Passengers.query.filter(Passengers.id == id).one_or_none()

    if passenger is not None:
        db.session.delete(passenger)
        db.session.commit()
        return make_response(
            f"Passenger {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Passenger not found for Id: {id}",
        )
