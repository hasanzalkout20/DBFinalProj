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

    