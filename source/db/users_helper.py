
from models import User, Ride, Car, Status, Route, user_schema, ride_schema, car_schema, status_schema, route_schema, passenger_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')

def read_all_users():
    users = User.query.all()
    return user_schema.dump(users)

def read_one(id):
    user = User.query.filter(User.id == id).first()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"id {id} not found"
        )


def create_user(user):
    id = user.get("id")
    existing_user = User.query.filter(User.id == id).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(
            406,
            f"User with id {id} already exists",
        )

def update_user(id, user):
    update_user = User.query.filter(User.id == id).one_or_none()

    if update_user is not None:
        schema = user_schema.load(user, session=db.session)
        update_user.name = schema.get('name')

        db.session.add(update_user)
        db.session.commit()

        data = user_schema.dump(update_user)

        return data, 200

    else:
        abort(
            404,
            f"User not found for Id: {id}",
        )

def delete_user(id):
    user = User.query.filter(User.id == id).one_or_none()

    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(
            f"User {id} deleted", 200
        )
    else:
        abort(
            404,
            f"User not found for Id: {id}",
        )
#==================================================================================
