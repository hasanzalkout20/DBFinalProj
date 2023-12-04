import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database = os.environ.get("DATABASE")
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

class Model:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def getProgramDepartments(self, department):
        self.cursor.execute("SELECT * FROM Program WHERE ProgDept = %s", (department,))
        programs = self.cursor.fetchall()
        return programs


    def getFacultyDepartments(self, name):
        self.cursor.execute('''
            SELECT Faculty.*, Program.ProgramName FROM Faculty 
            JOIN Program ON Program.LeadID = Faculty.FacultyID
            WHERE Faculty.DeptCode = %s
        ''', (name,))
        programs = self.cursor.fetchall()
        return programs

    def getProgramCourses(self, title):
        self.cursor.execute('''
            SELECT Course.*, CourseObjectives.*, SubObjectives.* FROM Course 
            WHERE Title = %s 
            JOIN CourseObjectives ON CourseObjectives.CourseID = Course.CourseID
            JOIN Program ON Program.ProgramName = CourseObjectives.ProgramName
            JOIN SubObjectives ON SubObjectives.SubObjCode = CourseObjectives.SubObjCode
            WHERE ProgramName = %s 
        ''', (title,))
        programs = self.cursor.fetchall()
        return programs

    def getProgramObjectives(self, program):
        self.cursor.execute("SELECT * FROM CourseObjectives WHERE Program = %s", (program,))
        programs = self.cursor.fetchall()
        return programs

    def getEvaluationResults(self, semester, year, secID):
        self.cursor.execute('''
            SELECT * FROM CourseObjectives 
            WHERE Semester = %s AND Year = %s AND SecID = %s
        ''', (semester, year, secID))
        programs = self.cursor.fetchall()
        return programs
    
    def getEvaluationResultsAcademicYear(self, year):
        self.cursor.execute('''
            SELECT ObjCode,
            Students,
            (100 * StudentsPassed / Students) AS PassPercentage
            FROM (
                SELECT *,
                SUM(Section.EnrollCount) AS Students
                FROM CourseObjectives 
                JOIN Section ON Section.SecID = CourseObjectives.SecID
                JOIN Objectives on Objectives.ObjCode = CourseObjectives.ObjCode
                WHERE Year = %s
                GROUP BY CourseObjectives.SecID
            ) AS Objectives
        ''', (year))
        programs = self.cursor.fetchall()
        return programs

# DATA ENTRY METHODS

    # Method to insert a new department
    def insert_department(self, deptName, deptCode):
        sql = "INSERT INTO Department (DeptName, DeptCode) VALUES (%s, %s)"
        self.cursor.execute(sql, (deptName, deptCode))
        self.connection.commit()

    # Method to insert a new faculty member
    def insert_faculty(self, name, email, deptID, position):
        sql = "INSERT INTO Faculty (Name, Email, DeptID, Position) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, email, deptID, position))
        self.connection.commit()

    # Method to insert a new program
    def insert_program(self, progName, deptID, facultyLeadID, facultyLeadEmail):
        sql = "INSERT INTO Program (ProgName, DeptID, FacultyLeadID, FacultyLeadEmail) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (progName, deptID, facultyLeadID, facultyLeadEmail))
        self.connection.commit()

    # Method to insert a new course
    def insert_course(self, deptID, title, description):
        sql = "INSERT INTO Course (DeptID, Title, Description) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (deptID, title, description))
        self.connection.commit()

    # Method to insert a new section
    def insert_section(self, courseID, semester, year, facultyLeadID, enrollCount):
        sql = "INSERT INTO Section (CourseID, Semester, Year, FacultyLeadID, EnrollCount) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (courseID, semester, year, facultyLeadID, enrollCount))
        self.connection.commit()

    # Method to insert a new objective
    def insert_objective(self, objCode, description, deptID):
        sql = "INSERT INTO Objectives (ObjCode, Description, DeptID) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (objCode, description, deptID))
        self.connection.commit()

    # Method to insert a new subobjective
    def insert_subobjective(self, subObjCode, description, parentObjID):
        sql = "INSERT INTO SubObjectives (SubObjCode, Description, ParentObjID) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (subObjCode, description, parentObjID))
        self.connection.commit()

    # Method to link a course to an objective
    def link_course_to_objective(self, courseID, objID):
        sql = "INSERT INTO CourseObjectives (CourseID, ObjID) VALUES (%s, %s)"
        self.cursor.execute(sql, (courseID, objID))
        self.connection.commit()

    # Method to enter evaluation results for a section
    def insert_evaluation_result(self, courseObjID, secID, semester, year, evalMethod, studentsPassed):
        sql = "INSERT INTO ObjectiveEval (CourseObjID, SecID, Semester, Year, EvalMethod, StudentsPassed) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (courseObjID, secID, semester, year, evalMethod, studentsPassed))
        self.connection.commit()
    