from flask_sqlalchemy import SQLAlchemy
from config import db, ma


class User(db.Model):
    __tablename__ = 'user_table'

    id = db.Column(db.Integer, primary_key=True)
    is_driver = db.Column(db.Boolean, nullable=False)
    id_car = db.Column(db.Integer, db.ForeignKey('car_table.id'))
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    car = db.relationship('Car', backref=db.backref('users'))

    def __init__(self, is_driver, id_car, email, password, phone):
        self.is_driver = is_driver
        self.id_car = id_car
        self.email = email
        self.password = password
        self.phone = phone


class Car(db.Model):
    __tablename__ = 'car_table'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    plate = db.Column(db.String(20), nullable=False)

    def __init__(self, brand, model, year, plate):
        self.brand = brand
        self.model = model
        self.year = year
        self.plate = plate


class Ride(db.Model):
    __tablename__ = 'ride_table'

    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    pickup = db.Column(db.String(100), nullable=False)
    drop_off = db.Column(db.String(100), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status_table.id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('route_table.id'), nullable=False)

    driver = db.relationship('User', backref=db.backref('rides'))
    status = db.relationship('Status')
    route = db.relationship('Route')

    def __init__(self, driver_id, start_time, end_time, pickup, drop_off, seats, status_id, route_id):
        self.driver_id = driver_id
        self.start_time = start_time
        self.end_time = end_time
        self.pickup = pickup
        self.drop_off = drop_off
        self.seats = seats
        self.status_id = status_id
        self.route_id = route_id


class Status(db.Model):
    __tablename__ = 'status_table'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, status):
        self.status = status


class Route(db.Model):
    __tablename__ = 'route_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name


class Passengers(db.Model):
    __tablename__ = 'passengers_table'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    ride_id = db.Column(db.Integer, db.ForeignKey('ride_table.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('passengers'))
    ride = db.relationship('Ride', backref=db.backref('passengers'))


# Define Marshmallow schemas for serialization and deserialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_fk = True


class CarSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Car
        load_instance = True
        sqla_session = db.session


class RideSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ride
        load_instance = True
        sqla_session = db.session
        include_fk = True


class StatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Status
        load_instance = True
        sqla_session = db.session


class RouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Route
        load_instance = True
        sqla_session = db.session


class PassengersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Passengers
        load_instance = True
        sqla_session = db.session


# Initialize the Marshmallow schemas

user_schema = UserSchema()
users_schema = UserSchema(many=True)

car_schema = CarSchema()
cars_schema = CarSchema(many=True)

ride_schema = RideSchema()
rides_schema = RideSchema(many=True)

status_schema = StatusSchema()
statuses_schema = StatusSchema(many=True)

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)

passenger_schema = PassengersSchema()
passengers_schema = PassengersSchema(many=True)
