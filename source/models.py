from datetime import datetime
from config import db, ma
from sqlalchemy import ForeignKey


# Print de prueba
print('models.py')

# Classes
# table_user


class User(db.Model):
    __tablename__ = "table_users"
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    phone = db.Column(db.Integer)
    oauth_key = db.Column(db.Integer)
    is_driver = db.Column(db.Integer)
    # Falta de agregrar ForeignKey('table_car.id')
    # P1
    # id_car = db.column(db.Integer, ForeignKey('table_car.id_car'))


# Schema User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_fk = True


user_schema = UserSchema()
user_schema_many = UserSchema(many=True)


# ----------------------------------------------------------------------------------------
# Classes
# table_rute


class Route(db.Model):
    __tablename__ = "table_route"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # No esta definida la variable DateTime
    date = db.Column(db.String(32))  # P1
    status = db.Column(db.String(32))
    cost_seat = db.Column(db.Integer)
    seats = db.Column(db.Integer)
    # No puse numero limite para el string
    pickup = db.Column(db.String(32))
    passengers = db.Column(db.String(32))


# Schema Route

class RouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Route
        load_instance = True
        sqla_session = db.session


route_schema = RouteSchema()
route_schema_many = RouteSchema(many=True)


# ---------------------------------------------------------------------------------------
# CLASS CAR


class Car(db.Model):
    __tablename__ = "table_car"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(32))
    year = db.Column(db.Integer)


# Schema Car

class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Car
        load_instance = True
        sqla_session = db.session


car_schema = CarSchema()
# Falta de agregar el people_schema por = ####
car_schema_many = CarSchema(many=True)
