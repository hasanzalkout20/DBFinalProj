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

# used for testing (clears tables and data)
def drop_tables():
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
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
                "Department"
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
                    CourseID VARCHAR(8) PRIMARY KEY,
                    DeptID INT NOT NULL,
                    Title VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Section (
                    SecID INT AUTO_INCREMENT PRIMARY KEY,
                    CourseID VARCHAR(8) NOT NULL,
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
                    CourseID VARCHAR(8) NOT NULL,
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
                """,
                """
                CREATE TABLE IF NOT EXISTS ProgramCourses (
                    ProgramCourseID INT AUTO_INCREMENT PRIMARY KEY,
                    ProgID INT NOT NULL,
                    CourseID VARCHAR(8) NOT NULL,
                    FOREIGN KEY (ProgID) REFERENCES Program(ProgID),
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    UNIQUE (ProgID, CourseID)
                    );
                """,
                """
                CREATE TABLE IF NOT EXISTS CourseProgramObjectives (
                    CourseProgObjID INT AUTO_INCREMENT PRIMARY KEY,
                    ProgramCourseID INT NOT NULL,
                    ObjID INT NOT NULL,
                    FOREIGN KEY (ProgramCourseID) REFERENCES ProgramCourses(ProgramCourseID),
                    FOREIGN KEY (ObjID) REFERENCES Objectives(ObjID),
                    UNIQUE (ProgramCourseID, ObjID)
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
#    drop_tables()    # uncomment to clear tables and data
    create_database()
    create_tables()
