import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database = os.environ.get("DATABASE")
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

# Function to create the database
def create_database():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            connection.commit()
            print(f"Database '{database}' created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Function to create the tables
def create_tables():
    # drop tables if they exist
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            commands = [
                "DROP TABLE IF EXISTS ObjectiveEval;",
                "DROP TABLE IF EXISTS CourseObjectives;",
                "DROP TABLE IF EXISTS SubObjectives;",
                "DROP TABLE IF EXISTS Objectives;",
                "DROP TABLE IF EXISTS Section;",
                "DROP TABLE IF EXISTS Course;",
                "DROP TABLE IF EXISTS Program;",
                "DROP TABLE IF EXISTS Faculty;",
                "DROP TABLE IF EXISTS Department;"
            ]
            for command in commands:
                cursor.execute(command)
            connection.commit()
            print("All tables dropped successfully")
            cursor.close()
    except Error as e:
        print(f"Error dropping tables: {e}")
    finally:
        if connection.is_connected():
            connection.close()
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            commands = [
                """
                CREATE TABLE IF NOT EXISTS Department (
                    DeptID INT AUTO_INCREMENT PRIMARY KEY,
                    DeptName VARCHAR(255) NOT NULL UNIQUE,
                    DeptCode CHAR(4) NOT NULL UNIQUE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Faculty (
                    FacultyID INT AUTO_INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) NOT NULL UNIQUE,
                    DeptID INT NOT NULL,
                    Position VARCHAR(255) NOT NULL,
                    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Program (
                    ProgID INT AUTO_INCREMENT PRIMARY KEY,
                    ProgName VARCHAR(255) NOT NULL UNIQUE,
                    DeptID INT NOT NULL,
                    FacultyLeadID INT NOT NULL,
                    FacultyLeadEmail VARCHAR(255) NOT NULL UNIQUE,
                    FOREIGN KEY (DeptID) REFERENCES Department(DeptID),
                    FOREIGN KEY (FacultyLeadID) REFERENCES Faculty(FacultyID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Course (
                    CourseID INT AUTO_INCREMENT PRIMARY KEY,
                    DeptID INT NOT NULL,
                    Title VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Section (
                    SecID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseID INT NOT NULL,
                    Semester VARCHAR(255) NOT NULL,
                    Year INT NOT NULL,
                    FacultyLeadID INT NOT NULL,
                    EnrollCount INT NOT NULL,
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (FacultyLeadID) REFERENCES Faculty(FacultyID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Objectives (
                    ObjID INT AUTO_INCREMENT PRIMARY KEY,
                    ObjCode VARCHAR(255) NOT NULL UNIQUE,
                    Description TEXT NOT NULL,
                    DeptID INT NOT NULL,
                    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS SubObjectives (
                    SubObjID INT AUTO_INCREMENT PRIMARY KEY,
                    SubObjCode VARCHAR(255) NOT NULL UNIQUE,
                    Description TEXT NOT NULL,
                    ParentObjID INT NOT NULL,
                    FOREIGN KEY (ParentObjID) REFERENCES Objectives(ObjID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS CourseObjectives (
                    CourseObjID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseID INT NOT NULL,
                    ObjID INT NOT NULL,
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (ObjID) REFERENCES Objectives(ObjID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS ObjectiveEval (
                    EvalID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseObjID INT NOT NULL,
                    SecID INT NOT NULL,
                    Semester VARCHAR(255) NOT NULL,
                    Year INT NOT NULL,
                    EvalMethod VARCHAR(255) NOT NULL,
                    StudentsPassed INT NOT NULL,
                    FOREIGN KEY (CourseObjID) REFERENCES CourseObjectives(CourseObjID),
                    FOREIGN KEY (SecID) REFERENCES Section(SecID)
                );
                """
            ]
            for command in commands:
                cursor.execute(command)
            connection.commit()
            print("All tables created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Main execution
if __name__ == "__main__":
    create_database()
    create_tables()


