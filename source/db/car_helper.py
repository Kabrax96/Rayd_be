# FILL
from models import Car, car_schema, car_schema_many
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')


def read_all():
    car = Car.query.all()
    return car_schema_many.dump(car)


def create(car):
    id = car.get("id")
    print('a ver id:', id)
    existing_car = Car.query.filter(Car.id == id).one_or_none()

    if existing_car is None:
        new_car = car_schema.load(car, session=db.session)
        db.session.add(new_car)
        db.session.commit()
        return car_schema.dump(new_car), 201
    else:
        abort(
            406,
            f"id {id} already exists",
        )


def read_one(id):
    car = Car.query.filter(Car.id == id).first()

    if car is not None:
        return car_schema.dump(car)
    else:
        abort(
            404, f"id {id} not found"
        )


def update(id, car):
    existing_car = Car.query.filter(Car.id == id).one_or_none()
    if existing_car:
        update_car = car_schema.load(car, session=db.session)
        existing_car.id = update_car.id  # se agregan otras tablas?
        db.session.commit()
        return car_schema.dump(existing_car), 201
    else:
        abort(
            404,
            f"id {id} not found"
        )


def delete(id):
    existing_car = Car.query.filter(Car.id == id).one_or_none()

    if existing_car:
        db.session.delete(existing_car)
        db.session.commit()
        return make_response(
            f"{id} successfully deleted", 200
        )

    else:
        abort(
            404,
            f"user with last name {id} not found"
        )
