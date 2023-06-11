

import sqlite3

def create_database():
    conn = sqlite3.connect('rayd.db')
    cursor = conn.cursor()

    # Create User table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
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
        CREATE TABLE IF NOT EXISTS Ride (
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
        CREATE TABLE IF NOT EXISTS Car (
            id INTEGER PRIMARY KEY,
            brand VARCHAR(50),
            model VARCHAR(50),
            year INTEGER,
            plate VARCHAR(20)
        )
    ''')

    # Create Status table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Status (
            id INTEGER PRIMARY KEY,
            status VARCHAR(50)
        )
    ''')

    # Create Route table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Route (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100)
        )
    ''')

    # Create Passenger table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Passenger (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            ride_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User (id),
            FOREIGN KEY (ride_id) REFERENCES Ride (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
