from models import Status, status_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')


# Status helper functions
def read_all_statuses():
    statuses = Status.query.all()
    return status_schema.dump(statuses)


def read_one(id):
    car = Status.query.filter(Status.id == id).first()

    if car is not None:
        return status_schema.dump(car)
    else:
        abort(
            404, f"id {id} not found"
        )


def create_status(status):
    id = status.get("id")
    existing_status = Status.query.filter(Status.id == id).one_or_none()

    if existing_status is None:
        new_status = status_schema.load(status, session=db.session)
        db.session.add(new_status)
        db.session.commit()
        return status_schema.dump(new_status), 201
    else:
        abort(
            406,
            f"Status with id {id} already exists",
        )


def update_status(id, status):
    update_status = Status.query.filter(Status.id == id).one_or_none()

    if update_status is not None:
        schema = status_schema.load(status, session=db.session)
        for key, value in schema.items():
            setattr(update_status, key, value)

        db.session.add(update_status)
        db.session.commit()

        data = status_schema.dump(update_status)

        return data, 200

    else:
        abort(
            404,
            f"Status not found for Id: {id}",
        )


def delete_status(id):
    status = Status.query.filter(Status.id == id).one_or_none()

    if status is not None:
        db.session.delete(status)
        db.session.commit()
        return make_response(
            f"Status {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Status not found for Id: {id}",
        )
