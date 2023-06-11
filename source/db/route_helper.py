# Fill
from models import Route, route_schema, route_schema_many
from config import db
from flask import make_response, abort
import sys
sys.path.append('../')

# Route helper functions
def read_all_routes():
    routes = Route.query.all()
    return route_schema.dump(routes)

def read_one(id):
    route = Route.query.filter(Route.id == id).first()

    if route is not None:
        return route_schema.dump(route)
    else:
        abort(
            404, f"id {id} not found"
        )


def create_route(route):
    id = route.get("id")
    existing_route = Route.query.filter(Route.id == id).one_or_none()

    if existing_route is None:
        new_route = route_schema.load(route, session=db.session)
        db.session.add(new_route)
        db.session.commit()
        return route_schema.dump(new_route), 201
    else:
        abort(
            406,
            f"Route with id {id} already exists",
        )

def update_route(id, route):
    update_route = Route.query.filter(Route.id == id).one_or_none()

    if update_route is not None:
        schema = route_schema.load(route, session=db.session)
        for key, value in schema.items():
            setattr(update_route, key, value)

        db.session.add(update_route)
        db.session.commit()

        data = route_schema.dump(update_route)

        return data, 200

    else:
        abort(
            404,
            f"Route not found for Id: {id}",
        )

def delete_route(id):
    route = Route.query.filter(Route.id == id).one_or_none()

    if route is not None:
        db.session.delete(route)
        db.session.commit()
        return make_response(
            f"Route {id} deleted", 200
        )
    else:
        abort(
            404,
            f"Route not found for Id: {id}",
        )


