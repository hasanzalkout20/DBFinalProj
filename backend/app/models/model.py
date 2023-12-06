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

    def getProgramDepartments(self, department_name):
    # Use a subquery to get the department ID from the department name
        self.cursor.execute('''
            SELECT ProgName
            FROM Program
            JOIN Department ON Program.DeptID = Department.DeptID
            WHERE Department.DeptName = %s
        ''', (department_name,))
        programs = self.cursor.fetchall()
        return programs

    def getFacultyByDepartmentName(self, department_name):
        self.cursor.execute('''
            SELECT Faculty.Name, Faculty.Email, Faculty.Position
            FROM Faculty
            INNER JOIN Department ON Faculty.DeptID = Department.DeptID
            WHERE Department.DeptName = %s
        ''', (department_name,))
        return self.cursor.fetchall()

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

    def getEvaluationResultsByCourseName(self, course_name, semester, year):
        self.cursor.execute('''
            SELECT ObjectiveEval.*
            FROM ObjectiveEval
            INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
            INNER JOIN Course ON Section.CourseID = Course.CourseID
            WHERE Course.Title = %s AND Section.Semester = %s AND Section.Year = %s
        ''', (course_name, semester, year))
        return self.cursor.fetchall()


    # DATA ENTRY METHODS

    # Method to insert a new department
    def insert_department(self, deptName, deptCode):
        try:
            sql = "INSERT INTO Department (DeptName, DeptCode) VALUES (%s, %s)"
            self.cursor.execute(sql, (deptName, deptCode))
            self.connection.commit()
            return {"message": "Department added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new faculty member
    def insert_faculty(self, name, email, deptID, position):
        try:
            sql = "INSERT INTO Faculty (Name, Email, DeptID, Position) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (name, email, deptID, position))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new program
    def insert_program(self, progName, deptID, facultyLeadID, facultyLeadEmail):
        try:
            sql = "INSERT INTO Program (ProgName, DeptID, FacultyLeadID, FacultyLeadEmail) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (progName, deptID, facultyLeadID, facultyLeadEmail))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}
    

    # Method to insert a new course
    def insert_course(self, deptID, title, description):
        try:
            sql = "INSERT INTO Course (DeptID, Title, Description) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (deptID, title, description))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}    
        

    # Method to insert a new section
    def insert_section(self, courseID, semester, year, facultyLeadID, enrollCount):
        try:
            sql = "INSERT INTO Section (CourseID, Semester, Year, FacultyLeadID, EnrollCount) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseID, semester, year, facultyLeadID, enrollCount))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new objective
    def insert_objective(self, objCode, description, deptID):
        try:
            sql = "INSERT INTO Objectives (ObjCode, Description, DeptID) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (objCode, description, deptID))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new subobjective
    def insert_subobjective(self, subObjCode, description, parentObjID):
        try:
            sql = "INSERT INTO SubObjectives (SubObjCode, Description, ParentObjID) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (subObjCode, description, parentObjID))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to link a course to an objective
    def link_course_to_objective(self, courseID, objID):
        try:
            sql = "INSERT INTO CourseObjectives (CourseID, ObjID) VALUES (%s, %s)"
            self.cursor.execute(sql, (courseID, objID))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to enter evaluation results for a section
    def insert_evaluation_result(self, courseObjID, secID, semester, year, evalMethod, studentsPassed):
        try:
            sql = "INSERT INTO ObjectiveEval (CourseObjID, SecID, Semester, Year, EvalMethod, StudentsPassed) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseObjID, secID, semester, year, evalMethod, studentsPassed))
            self.connection.commit()
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}
        

    