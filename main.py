import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='cs5330',
            password='Basketball20$'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS dbfinal")
            print("Database 'dbfinal' created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        if connection.is_connected():
            connection.close()

def create_tables():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='cs5330',
            password='Basketball20$',
            database='dbfinal'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            commands = [
                """
                CREATE TABLE IF NOT EXISTS Department (
                    DeptName VARCHAR(255) NOT NULL,
                    DeptCode CHAR(4) NOT NULL UNIQUE,
                    PRIMARY KEY (DeptName)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Faculty (
                    FacultyID INT NOT NULL AUTO_INCREMENT,
                    Name VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) NOT NULL UNIQUE,
                    DeptCode CHAR(4) NOT NULL,
                    `Rank` VARCHAR(255) NOT NULL,
                    PRIMARY KEY (FacultyID),
                    FOREIGN KEY (DeptCode) REFERENCES Department(DeptCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Program (
                    ProgramName VARCHAR(255) NOT NULL,
                    ProgDept CHAR(4) NOT NULL,
                    `Lead` VARCHAR(255) NOT NULL,
                    LeadID INT,
                    LeadEmail VARCHAR(255) NOT NULL,
                    PRIMARY KEY (ProgramName),
                    FOREIGN KEY (ProgDept) REFERENCES Department(DeptCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Course (
                    CourseID VARCHAR(255) NOT NULL,
                    Title VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    PRIMARY KEY (CourseID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Section (
                    SecID INT NOT NULL AUTO_INCREMENT,
                    CourseID VARCHAR(255) NOT NULL,
                    Semester VARCHAR(255) NOT NULL,
                    Year INT NOT NULL,
                    FacultyHeadID INT NOT NULL,
                    EnrollCount INT NOT NULL,
                    PRIMARY KEY (SecID),
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (FacultyHeadID) REFERENCES Faculty(FacultyID)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS Objectives (
                    ObjCode VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    ProgDept CHAR(4) NOT NULL,
                    PRIMARY KEY (ObjCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS SubObjectives (
                    SubObjCode VARCHAR(255) NOT NULL,
                    ProgDept CHAR(4) NOT NULL,
                    ParentObjCode VARCHAR(255) NOT NULL,
                    Description TEXT NOT NULL,
                    PRIMARY KEY (SubObjCode),
                    FOREIGN KEY (ParentObjCode) REFERENCES Objectives(ObjCode)
                );
                """,
                """
                CREATE TABLE IF NOT EXISTS CourseObjectives (
                    Program VARCHAR(255) NOT NULL,
                    CourseID VARCHAR(255) NOT NULL,
                    SecID INT NOT NULL,
                    Semester VARCHAR(255) NOT NULL,
                    Year INT NOT NULL,
                    ObjCode VARCHAR(255) NOT NULL,
                    SubObjCode VARCHAR(255) NOT NULL,
                    EvalMethod VARCHAR(255) NOT NULL,
                    StudentsPassed INT NOT NULL,
                    FOREIGN KEY (Program) REFERENCES Program(ProgramName),
                    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
                    FOREIGN KEY (SecID) REFERENCES Section(SecID),
                    FOREIGN KEY (ObjCode) REFERENCES Objectives(ObjCode),
                    FOREIGN KEY (SubObjCode) REFERENCES SubObjectives(SubObjCode)
                );
                """
            ]
            for command in commands:
                cursor.execute(command)
            print("All tables created successfully")
            cursor.close()
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()


