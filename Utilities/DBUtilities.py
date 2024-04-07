import os
import sqlite3

class DBUtils:
    def InitializeDB():
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()

        # Create the 'attraction' table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attraction
            ([attraction_id] INTEGER PRIMARY KEY, 
            [attraction_name] TEXT UNIQUE, 
            [attraction_openinghours] TEXT, 
            [attraction_ticketprice] INTEGER, 
            [attraction_capacity] INTEGER
            )
        ''')

        # Create the 'feedback' table with the 'attraction_id' foreign key
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback
            ([feedback_id] INTEGER PRIMARY KEY, 
            [feedback_content] TEXT,
            [attraction_id] INTEGER,
            FOREIGN KEY (attraction_id) REFERENCES attraction(attraction_id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS booking
            ([booking_id] INTEGER PRIMARY KEY, 
            [booking_customer] TEXT,
            [booking_hotel] TEXT,
            [booking_room_type] TEXT,
            [booking_number_of_rooms] INTEGER,
            [booking_number_of_nights] INTEGER,
            [booking_cost] INTEGER
            )
        ''')

        connection.commit()
        return connection