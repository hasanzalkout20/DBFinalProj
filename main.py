import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host='localhost',
            user='cs5330',
            # Ensure you replace 'your_password' with the actual password.
            password='your_password'
        )

        # Check if connection was successful
        if connection.is_connected():
            # Cursor creation
            cursor = connection.cursor()
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS dbfinal")
            print("Database created successfully")
    except Error as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

create_database()

