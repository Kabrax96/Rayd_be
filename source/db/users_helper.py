
from models import User, route_schema_many, user_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')


def read_all():
    people = User.query.all()
    return route_schema_many.dump(people)


def create(user):
    id = User.get("id")
    print('a ver id:', id)
    existing_user = User.query.filter(User.id == id).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(
            406,
            f"id {id} already exists",
        )


def read_one(id):
    user = User.query.filter(User.id == id).first()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"id {id} not found"
        )


def update(id, user):
    existing_user = User.query.filter(User.id == id).one_or_none()
    if existing_user:
        update_user = user_schema.load(user, session=db.session)
        existing_user.id = update_user.id  # se agregan otras tablas?
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(
            404,
            f"id {id} not found"
        )


def delete(id):
    existing_user = User.query.filter(User.id == id).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(
            f"{id} successfully deleted", 200
        )

    else:
        abort(
            404,
            f"user with last name {id} not found"
        )
