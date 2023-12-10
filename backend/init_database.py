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

# Used for testing (clears tables and data)
def drop_tables():
    try:
        connection = mysql.connector.connect(
            host=host, user=username, password=password, database=database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            tables = [
                "CourseProgramObjectives",
                "ProgramCourses",
                "ObjectiveEval",
                "CourseObjectives",
                "SubObjectives",
                "Objectives",
                "Section",
                "Course",
                "Program",
                "Faculty",
                "Department",
            ]
            for table in tables:
                cursor.execute(f"DROP TABLE IF EXISTS {table}")
                print(f"Table '{table}' dropped successfully")
            connection.commit()
            cursor.close()
    except Error as e:
        print(f"Error dropping tables: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Function to create the database
def create_database():
    try:
        connection = mysql.connector.connect(
            host=host, user=username, password=password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print("Database created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Function to create the tables
def create_tables():
    try:
        connection = mysql.connector.connect(
            host=host, user=username, password=password, database=database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            commands = [
                """
                CREATE TABLE IF NOT EXISTS Department (
                    DeptCode CHAR(4) PRIMARY KEY,
                    DeptName VARCHAR(255) NOT NULL UNIQUE
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Faculty (
                    FacultyID INT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) NOT NULL UNIQUE,
                    DeptCode CHAR(4) NOT NULL,
                    Position ENUM('Full', 'Associate', 'Assistant', 'Adjunct') NOT NULL,
                    FOREIGN KEY (DeptCode) REFERENCES Department(DeptCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Program (
                    ProgramName VARCHAR(255) PRIMARY KEY,
                    DeptCode CHAR(4) NOT NULL,
                    FacultyLeadName VARCHAR(255) NOT NULL,
                    FacultyLeadID INT NOT NULL,
                    FacultyLeadEmail VARCHAR(255) NOT NULL,
                    FOREIGN KEY (DeptCode) REFERENCES Department(DeptCode),
                    FOREIGN KEY (FacultyLeadID) REFERENCES Faculty(FacultyID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Course (
                    CourseID VARCHAR(8) PRIMARY KEY,
                    DeptCode CHAR(4) NOT NULL,
                    Title VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    FOREIGN KEY (DeptCode) REFERENCES Department(DeptCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Section (
                    SectionID VARCHAR(20) PRIMARY KEY,
                    CourseID VARCHAR(8) NOT NULL,
                    Semester ENUM('Fall', 'Spring', 'Summer') NOT NULL,
                    Year INT NOT NULL,
                    FacultyLeadID INT NOT NULL,
                    EnrollCount INT NOT NULL,
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (FacultyLeadID) REFERENCES Faculty(FacultyID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Objectives (
                    ObjCode VARCHAR(255) PRIMARY KEY,
                    Description TEXT NOT NULL,
                    ProgramName VARCHAR(255) NOT NULL,
                    FOREIGN KEY (ProgramName) REFERENCES Program(ProgramName)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS SubObjectives (
                    SubObjCode VARCHAR(255) PRIMARY KEY,
                    Description TEXT NOT NULL,
                    ObjCode VARCHAR(255) NOT NULL,
                    FOREIGN KEY (ObjCode) REFERENCES Objectives(ObjCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS CourseObjectives (
                    CourseObjID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseID VARCHAR(8) NOT NULL,
                    ObjCode VARCHAR(255) NOT NULL,
                    SubObjCode VARCHAR(255),
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (ObjCode) REFERENCES Objectives(ObjCode),
                    FOREIGN KEY (SubObjCode) REFERENCES SubObjectives(SubObjCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS ObjectiveEval (
                    ObjEvalID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseObjID INT NOT NULL,
                    SectionID VARCHAR(20) NOT NULL,
                    EvalMethod ENUM('Exam', 'Homework', 'Project') NOT NULL,
                    StudentsPassed INT NOT NULL,
                    FOREIGN KEY (CourseObjID) REFERENCES CourseObjectives(CourseObjID),
                    FOREIGN KEY (SectionID) REFERENCES Section(SectionID)
                );
                """
            ]
            for command in commands:
                cursor.execute(command)
                connection.commit()
            print("Tables created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection.is_connected():
            connection.close()

# Main execution
if __name__ == "__main__":
#    drop_tables()
    create_database()
    create_tables()

