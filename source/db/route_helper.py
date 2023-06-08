# Fill
from models import Route, route_schema, route_schema_many
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')


def read_all():
    route = Route.query.all()
    return route_schema_many.dump(route)


def create(route):
    id = route.get("id")
    print('a ver id route:', id)
    existing_route = Route.query.filter(Route.id == id).one_or_none()

    if existing_route is None:
        new_route = route_schema.load(route, session=db.session)
        db.session.add(new_route)
        db.session.commit()
        return route_schema.dump(new_route), 201
    else:
        abort(
            406,
            f"id {id} already exists",
        )


def read_one(id):
    route = Route.query.filter(Route.id == id).first()

    if route is not None:
        return route_schema.dump(route)
    else:
        abort(
            404, f"id {id} not found"
        )


def update(id, route):
    existing_route = Route.query.filter(Route.id == id).one_or_none()
    if existing_route:
        update_route = route_schema.load(route, session=db.session)
        existing_route.id = update_route.id  # se agregan otras tablas?
        db.session.commit()
        return route_schema.dump(existing_route), 201
    else:
        abort(
            404,
            f"id {id} not found"
        )


def delete(id):
    existing_route = Route.query.filter(Route.id == id).one_or_none()

    if existing_route:
        db.session.delete(existing_route)
        db.session.commit()
        return make_response(
            f"{id} successfully deleted", 200
        )

    else:
        abort(
            404,
            f"user with last name {id} not found"
        )
