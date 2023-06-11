# FILL
from models import Car, car_schema
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')


# Car helper functions
def read_all_cars():
    cars = Car.query.all()
    return car_schema.dump(cars)


def read_one(id):
    car = Car.query.filter(Car.id == id).first()

    if car is not None:
        return car_schema.dump(car)
    else:
        abort(
            404, f"id {id} not found"
        )


def create_car(car):
    id = car.get("id")
    existing_car = Car.query.filter(Car.id == id).one_or_none()

    if existing_car is None:
        new_car = car_schema.load(car, session=db.session)
        db.session.add(new_car)
        db.session.commit()
        return car_schema.dump(new_car), 201
    else:
        abort(
            406,
            f"Car with id {id} already exists",
        )


def update_car(id, car):
    update_car = Car.query.filter(Car.id == id).one_or_none()

    if update_car is not None:
        schema = car_schema.load(car, session=db.session)
        for key, value in schema.items():
            setattr(update_car, key, value)

        db.session.add(update_car)
        db.session.commit()

        data = car_schema.dump(update_car)

        return data, 200

    else:
        abort(
            404,
            f"Car not found for Id: {id}",
        )


def delete_car(id):
    car = Car.query.filter(Car.id == id).one_or_none()

    if car is not None:
        db.session.delete(car)
        db.session.commit()
        return make_response(
            f"Car {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Car not found for Id: {id}",
        )
