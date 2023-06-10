# Database Schema

This documentation provides an overview of the database schema, including the tables and their respective columns, data types, and descriptions.

## User Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a user
is_driver | BOOLEAN | Flag indicating if the user is a driver or not
id_car | INT | Foreign key to the Car table (associated car)
email | VARCHAR(100) | User's email address
password | VARCHAR(100) | User's password
phone | VARCHAR(20) | User's phone number

## Ride Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a ride
driver_id | INT | Foreign key to the User table (driver user)
start_time | DATETIME | Start time of the ride
end_time | DATETIME | End time of the ride
pickup | VARCHAR(100) | Pickup location
drop_off | VARCHAR(100) | Drop-off location
seats | INT | Number of available seats in the ride
status_id | INT | Foreign key to the Status table (status of the ride)
route_id | INT | Foreign key to the Route table (associated route)

## Car Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a car
brand | VARCHAR(50) | Brand or manufacturer of the car
model | VARCHAR(50) | Model of the car
year | INT | Year of the car
plate | VARCHAR(20) | License plate number of the car

## Status Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a status
status | VARCHAR(50) | Name or description of the status

## Route Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a route
name | VARCHAR(100) | Name or description of the route

## Passengers Table
Column | Data Type | Description
--- | --- | ---
id | INT | Unique identifier for a passenger
user_id | INT | Foreign key to the User table (passenger user)
ride_id | INT | Foreign key to the Ride table (associated ride)

# Diagrams

## Simple Diagram
The simple diagram represents the relationships between the tables in a simplified manner. It shows how the tables are connected through their respective foreign keys.

```
graph LR
  A[User] -- is_driver --> C((Car))
  A -- id --> D[Ride]
  A -- id --> E[Passengers]
  D -- driver_id --> A
  D -- status_id --> F[Status]
  D -- route_id --> G[Route]
  C -- id --> D
  E -- user_id --> A
  E -- ride_id --> D
```

Explanation:
- The `User` table has a one-to-one relationship with the `Car` table through the `id_car` foreign key.
- The `User` table has a one-to-many relationship with the `Ride` table through the `id` foreign key.
- The `User` table has a one-to-many relationship with the `Passengers` table through the `id` foreign key.
- The `Ride` table has a many-to-one relationship with the `User` table through the `driver_id` foreign key.
- The `Ride` table has a many-to-one relationship with the `Status` table through the `status_id` foreign key.
- The `Ride` table has a many-to-one relationship with the `Route` table through the `route_id` foreign key.
- The `Car` table has a one-to-one relationship with the `Ride` table through the `id` foreign key.
- The `Passengers` table has a many-to-one relationship with the `User` table through the `user_id` foreign key.
- The `Passengers` table has a many-to-one relationship with the `Ride` table through the `ride_id` foreign key.

## Detailed Diagram
The detailed diagram provides a more comprehensive view of the tables and their attributes, along with the relationships between them.

```
flowchart LR
  subgraph User
    id(User.id)
    is_driver(User.is_driver)
    id_car(User.id_car)
    email(User.email)
    password(User.password)
    phone(User.phone)
  end

  subgraph Car
    id(Car.id)
    brand(Car.brand)
    model(Car.model)
    year(Car.year)
    plate(Car.plate)
  end

  subgraph Ride
    id(Ride.id)
    driver_id(Ride.driver_id)
    start_time(Ride.start_time)
    end_time(Ride.end_time)
    pickup(Ride.pickup)
    drop_off(Ride.drop_off)
    seats(Ride.seats)
    status_id(Ride.status_id)
    route_id(Ride.route_id)
  end

  subgraph Status
    id(Status.id)
    status(Status.status)
  end

  subgraph Route
    id(Route.id)
    name(Route.name)
  end

  subgraph Passengers
    id(Passengers.id)
    user_id(Passengers.user_id)
    ride_id(Passengers.ride_id)
  end

  id_car -- id --> Car
  driver_id -- id --> User
  status_id -- id --> Status
  route_id -- id --> Route
  user_id -- id --> User
  ride_id -- id --> Ride
```

Explanation:
- The diagram represents each table as a subgraph with its respective attributes.
- Arrows indicate the relationships between tables through their foreign keys.
- For example, `id_car` in the `User` table points to the `id` attribute in the `Car` table, representing the association between a user and their associated car