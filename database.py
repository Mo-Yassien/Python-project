import sqlite3
import os

def create_connection():
    """Create a database connection"""
    try:
        conn = sqlite3.connect('reservations.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_database():
    """Initialize the database with required tables"""
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    flight_number TEXT NOT NULL,
                    departure TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    date TEXT NOT NULL,
                    seat_number TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

def create_reservation(conn, reservation):
    """Create a new reservation"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', reservation)
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error creating reservation: {e}")
        return None

def get_all_reservations(conn):
    """Get all reservations"""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error getting reservations: {e}")
        return []

def get_reservation(conn, reservation_id):
    """Get a specific reservation by ID"""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error getting reservation: {e}")
        return None

def update_reservation(conn, reservation):
    """Update a reservation"""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE reservations 
            SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
            WHERE id = ?
        ''', reservation)
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error updating reservation: {e}")
        return False

def delete_reservation(conn, reservation_id):
    """Delete a reservation"""
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error deleting reservation: {e}")
        return False 