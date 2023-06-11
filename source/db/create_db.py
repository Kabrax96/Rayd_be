

import sqlite3
from faker import Faker
from datetime import datetime, timedelta

def create_database():
    
    fake = Faker()

    conn = sqlite3.connect('rayd.db')
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_table (
            id INTEGER PRIMARY KEY,
            is_driver BOOLEAN,
            id_car INTEGER,
            email VARCHAR(100),
            password VARCHAR(100),
            phone VARCHAR(20)
        )
    ''')

    # Create Ride table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rayd_table (
            id INTEGER PRIMARY KEY,
            driver_id INTEGER,
            start_time DATETIME,
            end_time DATETIME,
            pickup VARCHAR(100),
            drop_off VARCHAR(100),
            seats INTEGER,
            status_id INTEGER,
            route_id INTEGER,
            FOREIGN KEY (driver_id) REFERENCES User (id),
            FOREIGN KEY (status_id) REFERENCES Status (id),
            FOREIGN KEY (route_id) REFERENCES Route (id)
        )
    ''')

    # Create Car table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car_table (
            id INTEGER PRIMARY KEY,
            brand VARCHAR(50),
            model VARCHAR(50),
            year INTEGER,
            plate VARCHAR(20)
        )
    ''')

    # Create Status table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status_table (
            id INTEGER PRIMARY KEY,
            status VARCHAR(50)
        )
    ''')

    # Create Route table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS route_table (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100)
        )
    ''')

    # Create Passenger table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passengers_table (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            ride_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User (id),
            FOREIGN KEY (ride_id) REFERENCES Ride (id)
        )
    ''')


    # Add dummy data
    for _ in range(5):
        # Generate a random user
        is_driver = fake.boolean()
        email = fake.email()
        password = fake.password()
        phone = fake.phone_number()
        cursor.execute(
            "INSERT INTO user_table (is_driver, email, password, phone) VALUES (?, ?, ?, ?)",
            (is_driver, email, password, phone)
        )
        user_id = cursor.lastrowid

        if is_driver:
            # Generate a car for the driver
            brand = fake.word()
            model = fake.word()
            year = fake.random_int(min=2000, max=2023)
            plate = fake.license_plate()
            cursor.execute(
                "INSERT INTO car_table (brand, model, year, plate) VALUES (?, ?, ?, ?)",
                (brand, model, year, plate)
            )
            car_id = cursor.lastrowid

            # Update the user's car ID
            cursor.execute(
                "UPDATE user_table SET id_car = ? WHERE id = ?",
                (car_id, user_id)
            )

        # Generate a random ride
        start_time = fake.date_time_between(start_date="-1d", end_date="+1d")
        end_time = start_time + timedelta(hours=fake.random_int(min=1, max=4))
        pickup = fake.address()
        drop_off = fake.address()
        seats = fake.random_int(min=1, max=4)
        status_id = fake.random_int(min=1, max=3)
        route_id = fake.random_int(min=1, max=3)
        cursor.execute(
            "INSERT INTO rayd_table (driver_id, start_time, end_time, pickup, drop_off, seats, status_id, route_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, start_time, end_time, pickup, drop_off, seats, status_id, route_id)
        )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
