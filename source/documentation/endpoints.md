# API Endpoints Documentation

## User Endpoints
Retrieves and manages user data.

| Endpoint                | Method | Description                        | Required Parameters |
| ----------------------- | ------ | ---------------------------------- | ------------------- |
| `/users`                | GET    | Retrieves a list of all users.     | -                   |
| `/users/{user_id}`      | GET    | Retrieves a specific user by ID.   | `user_id`           |
| `/users`                | POST   | Creates a new user.                | -                   |
| `/users/{user_id}`      | PUT    | Updates an existing user by ID.    | `user_id`           |
| `/users/{user_id}`      | DELETE | Deletes a user by ID.              | `user_id`           |

## Car Endpoints
Retrieves and manages car data.

| Endpoint                | Method | Description                        | Required Parameters |
| ----------------------- | ------ | ---------------------------------- | ------------------- |
| `/cars`                 | GET    | Retrieves a list of all cars.      | -                   |
| `/cars/{car_id}`        | GET    | Retrieves a specific car by ID.    | `car_id`            |
| `/cars`                 | POST   | Creates a new car.                 | -                   |
| `/cars/{car_id}`        | PUT    | Updates an existing car by ID.     | `car_id`            |
| `/cars/{car_id}`        | DELETE | Deletes a car by ID.               | `car_id`            |

## Ride Endpoints
Retrieves and manages ride data.

| Endpoint                | Method | Description                        | Required Parameters |
| ----------------------- | ------ | ---------------------------------- | ------------------- |
| `/rides`                | GET    | Retrieves a list of all rides.     | -                   |
| `/rides/{ride_id}`      | GET    | Retrieves a specific ride by ID.   | `ride_id`           |
| `/rides`                | POST   | Creates a new ride.                | -                   |
| `/rides/{ride_id}`      | PUT    | Updates an existing ride by ID.    | `ride_id`           |
| `/rides/{ride_id}`      | DELETE | Deletes a ride by ID.              | `ride_id`           |

## Status Endpoints
Retrieves and manages status data.

| Endpoint                | Method | Description                        | Required Parameters |
| ----------------------- | ------ | ---------------------------------- | ------------------- |
| `/statuses`             | GET    | Retrieves a list of all statuses.  | -                   |
| `/statuses/{status_id}` | GET    | Retrieves a specific status by ID. | `status_id`         |

## Route Endpoints
Retrieves and manages route data.

| Endpoint                | Method | Description                        | Required Parameters |
| ----------------------- | ------ | ---------------------------------- | ------------------- |
| `/routes`               | GET    | Retrieves a list of all routes.    | -                   |
| `/routes/{route_id}`    | GET    | Retrieves a specific route by ID.  | `route_id`          |

## Passengers Endpoints
Retrieves and manages passenger data for rides.

| Endpoint                          | Method | Description                                     | Required Parameters |
| --------------------------------- | ------ | ----------------------------------------------- | ------------------- |
| `/rides/{ride_id}/passengers`      | GET    | Retrieves a list of passengers for a ride.      | `ride_id`           |
| `/rides/{ride_id}/passengers`      | POST   | Adds a passenger to a ride.                     | `ride_id`           |
| `/rides

/{ride_id}/passengers/{passenger_id}` | DELETE | Removes a passenger from a ride.                | `ride_id`, `passenger_id` |

