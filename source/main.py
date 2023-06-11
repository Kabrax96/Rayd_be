
import config
from flask import Flask, jsonify, request, render_template
from models import User, Ride, Car, Status, Route, Passengers
# from schemas import user_schema, ride_schema, car_schema, status_schema, route_schema, passenger_schema

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
# Definiendo una funcion (home)
# Renderisa una variable a render_tamplate de Home.htlm
def home():
    people = User.query.all()
    return render_template("home.html/", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
# User routes
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify(user_schema.dump(users))

# @app.route('/users', methods=['POST'])
# def create_user():
#     user_data = request.get_json()
#     new_user = User(**user_data)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(user_schema.dump(new_user)), 201

# @app.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id)
#     if user is None:
#         return jsonify(message='User not found'), 404
#     return jsonify(user_schema.dump(user))

# @app.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     if user is None:
#         return jsonify(message='User not found'), 404
#     user_data = request.get_json()
#     user.is_driver = user_data.get('is_driver', user.is_driver)
#     user.id_car = user_data.get('id_car', user.id_car)
#     user.email = user_data.get('email', user.email)
#     user.password = user_data.get('password', user.password)
#     user.phone = user_data.get('phone', user.phone)
#     db.session.commit()
#     return jsonify(user_schema.dump(user))

# @app.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if user is None:
#         return jsonify(message='User not found'), 404
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify(message='User deleted'), 200

# # Ride routes
# @app.route('/rides', methods=['GET'])
# def get_all_rides():
#     rides = Ride.query.all()
#     return jsonify(ride_schema.dump(rides))

# @app.route('/rides', methods=['POST'])
# def create_ride():
#     ride_data = request.get_json()
#     new_ride = Ride(**ride_data)
#     db.session.add(new_ride)
#     db.session.commit()
#     return jsonify(ride_schema.dump(new_ride)), 201

# Car routes, Status routes, Route routes, Passenger routes (similar structure as User and Ride routes)