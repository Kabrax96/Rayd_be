from models import Ride, ride_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')

# Ride helper functions


def read_all_rides():
    rides = Ride.query.all()
    return ride_schema.dump(rides)


def read_one(id):
    car = Ride.query.filter(Ride.id == id).first()

    if car is not None:
        return ride_schema.dump(car)
    else:
        abort(
            404, f"id {id} not found"
        )


def create_ride(ride):
    id = ride.get("id")
    existing_ride = Ride.query.filter(Ride.id == id).one_or_none()

    if existing_ride is None:
        new_ride = ride_schema.load(ride, session=db.session)
        db.session.add(new_ride)
        db.session.commit()
        return ride_schema.dump(new_ride), 201
    else:
        abort(
            406,
            f"Ride with id {id} already exists",
        )


def update_ride(id, ride):
    update_ride = Ride.query.filter(Ride.id == id).one_or_none()

    if update_ride is not None:
        schema = ride_schema.load(ride, session=db.session)
        for key, value in schema.items():
            setattr(update_ride, key, value)

        db.session.add(update_ride)
        db.session.commit()

        data = ride_schema.dump(update_ride)

        return data, 200

    else:
        abort(
            404,
            f"Ride not found for Id: {id}",
        )


def delete_ride(id):
    ride = Ride.query.filter(Ride.id == id).one_or_none()

    if ride is not None:
        db.session.delete(ride)
        db.session.commit()
        return make_response(
            f"Ride {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Ride not found for Id: {id}",
        )
