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

    def getProgramCourses(self, program_name):
        self.cursor.execute('''
            SELECT Course.*, CourseObjectives.*, SubObjectives.* 
            FROM Course
            JOIN CourseObjectives ON Course.CourseID = CourseObjectives.CourseID
            JOIN ProgramCourses ON ProgramCourses.CourseID = Course.CourseID
            JOIN Program ON Program.ProgID = ProgramCourses.ProgID
            LEFT JOIN SubObjectives ON CourseObjectives.ObjID = SubObjectives.ParentObjID
            WHERE Program.ProgName = %s
        ''', (program_name,))
        return self.cursor.fetchall()

    def getProgramObjectives(self, program_name):       
        self.cursor.execute('''
            SELECT Objectives.ObjCode, Objectives.Description
            FROM Objectives
            JOIN CourseObjectives ON Objectives.ObjID = CourseObjectives.ObjID
            JOIN Course ON Course.CourseID = CourseObjectives.CourseID
            JOIN ProgramCourses ON Course.CourseID = ProgramCourses.CourseID
            JOIN Program ON Program.ProgID = ProgramCourses.ProgID
            WHERE Program.ProgName = %s
        ''', (program_name,))
        return self.cursor.fetchall()

    def getEvaluationResultsByCourseName(self, course_name, semester, year):
        self.cursor.execute('''
            SELECT ObjectiveEval.*
            FROM ObjectiveEval
            INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
            INNER JOIN Course ON Section.CourseID = Course.CourseID
            WHERE Course.Title = %s AND Section.Semester = %s AND Section.Year = %s
        ''', (course_name, semester, year))
        return self.cursor.fetchall()
    
    # def getEvaluationResultsByProgramAndSemester(self, program_name, semester, year):
    #     try:
    #         self.cursor.execute('''
    #             SELECT Section.SecID, Course.Title, ObjectiveEval.*
    #             FROM ObjectiveEval
    #             INNER JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
    #             INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
    #             INNER JOIN Course ON Course.CourseID = Section.CourseID
    #             INNER JOIN ProgramCourses ON Course.CourseID = ProgramCourses.CourseID
    #             INNER JOIN Program ON Program.ProgID = ProgramCourses.ProgID
    #             WHERE Program.ProgName = %s AND Section.Semester = %s AND Section.Year = %s
    #         ''', (program_name, semester, year))
    #         return self.cursor.fetchall()
    #     except Error as e:
    #         return {"error": str(e)}
    def getEvaluationResultsByProgramAndSemester(self, program_name, semester, year):
        try:
            self.cursor.execute('''
                SELECT Course.Title AS CourseTitle, Section.Semester, Section.Year, Faculty.Name AS FacultyName, 
                       Objectives.ObjCode, SubObjectives.SubObjCode, ObjectiveEval.EvalMethod, ObjectiveEval.StudentsPassed
                FROM ObjectiveEval
                INNER JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
                INNER JOIN Objectives ON CourseObjectives.ObjID = Objectives.ObjID
                LEFT JOIN SubObjectives ON Objectives.ObjID = SubObjectives.ParentObjID
                INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
                INNER JOIN Course ON Section.CourseID = Course.CourseID
                INNER JOIN Faculty ON Section.FacultyLeadID = Faculty.FacultyID
                INNER JOIN ProgramCourses ON Course.CourseID = ProgramCourses.CourseID
                INNER JOIN Program ON Program.ProgID = ProgramCourses.ProgID
                WHERE Program.ProgName = %s AND Section.Semester = %s AND Section.Year = %s
            ''', (program_name, semester, year))
            return self.cursor.fetchall()
        except Error as e:
            return {"error": str(e)}
    
    # def getEvaluationResultsByAcademicYear(self, academic_year):
    #     self.cursor.execute('''
    #         SELECT ObjectiveEval.*, Objectives.ObjCode, SubObjectives.SubObjCode
    #         FROM ObjectiveEval
    #         JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
    #         JOIN Objectives ON CourseObjectives.ObjID = Objectives.ObjID
    #         LEFT JOIN SubObjectives ON Objectives.ObjID = SubObjectives.ParentObjID
    #         JOIN Section ON ObjectiveEval.SecID = Section.SecID
    #         WHERE Section.Year = %s
    #     ''', (academic_year,))
    #     return self.cursor.fetchall()
    
    # Modified method to get evaluation results by academic year
    def getEvaluationResultsByAcademicYear(self, academic_year):
        try:
            self.cursor.execute('''
                SELECT Course.Title AS CourseTitle, Section.Semester, Section.Year, Faculty.Name AS FacultyName, 
                       Objectives.ObjCode, SubObjectives.SubObjCode, ObjectiveEval.EvalMethod, ObjectiveEval.StudentsPassed
                FROM ObjectiveEval
                INNER JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
                INNER JOIN Objectives ON CourseObjectives.ObjID = Objectives.ObjID
                LEFT JOIN SubObjectives ON Objectives.ObjID = SubObjectives.ParentObjID
                INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
                INNER JOIN Course ON Section.CourseID = Course.CourseID
                INNER JOIN Faculty ON Section.FacultyLeadID = Faculty.FacultyID
                WHERE Section.Year = %s
            ''', (academic_year,))
            return self.cursor.fetchall()
        except Error as e:
            return {"error": str(e)}
    
    def getCoursesAndObjectivesForProgram(self, program_name):
        self.cursor.execute('''
            SELECT Course.Title, Objectives.ObjCode, SubObjectives.SubObjCode 
            FROM Course
            JOIN CourseObjectives ON Course.CourseID = CourseObjectives.CourseID
            JOIN Objectives ON CourseObjectives.ObjID = Objectives.ObjID
            LEFT JOIN SubObjectives ON Objectives.ObjID = SubObjectives.ParentObjID
            WHERE Course.DeptID IN (SELECT DeptID FROM Program WHERE ProgName = %s)
        ''', (program_name,))
        return self.cursor.fetchall()

    # DATA ENTRY METHODS

    # Method to insert a new department
    def insert_department(self, deptCode, deptName):
        try:
            self.cursor.execute("SELECT DeptCode FROM Department WHERE DeptCode = %s", (deptCode,))
            if self.cursor.fetchone():
                return {"message": "Department code already exists"}
            sql = "INSERT INTO Department (DeptCode, DeptName) VALUES (%s, %s)"
            self.cursor.execute(sql, (deptCode, deptName))
            self.connection.commit()
            return {"message": "Department added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new faculty member
    def insert_faculty(self, facultyID, name, email, deptCode, position):
        try:
            self.cursor.execute("SELECT FacultyID FROM Faculty WHERE FacultyID = %s OR Email = %s", (facultyID, email))
            if self.cursor.fetchone():
                return {"message": "Faculty member already exists"}
            sql = "INSERT INTO Faculty (FacultyID, Name, Email, DeptCode, Position) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (facultyID, name, email, deptCode, position))
            self.connection.commit()
            return {"message": "Faculty member added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new program
    def insert_program(self, programName, deptCode, facultyLeadName, facultyLeadID, facultyLeadEmail):
        try:
            self.cursor.execute("SELECT ProgramName FROM Program WHERE ProgramName = %s", (programName,))
            if self.cursor.fetchone():
                return {"message": "Program already exists"}
            sql = "INSERT INTO Program (ProgramName, DeptCode, FacultyLeadName, FacultyLeadID, FacultyLeadEmail) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (programName, deptCode, facultyLeadName, facultyLeadID, facultyLeadEmail))
            self.connection.commit()
            return {"message": "Program added successfully"}
        except Error as e:
            return {"error": str(e)}


    # Method to insert a new course
    def insert_course(self, courseID, deptCode, title, description):
        try:
            self.cursor.execute("SELECT CourseID FROM Course WHERE CourseID = %s", (courseID,))
            if self.cursor.fetchone():
                return {"message": "Course with this ID already exists"}
            sql = "INSERT INTO Course (CourseID, DeptCode, Title, Description) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (courseID, deptCode, title, description))
            self.connection.commit()
            return {"message": "Course added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new section
    def insert_section(self, sectionID, courseID, semester, year, facultyLeadID, enrollCount):
        try:
            self.cursor.execute("SELECT SectionID FROM Section WHERE SectionID = %s", (sectionID,))
            if self.cursor.fetchone():
                return {"message": "Section ID already exists"}
            sql = "INSERT INTO Section (SectionID, CourseID, Semester, Year, FacultyLeadID, EnrollCount) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (sectionID, courseID, semester, year, facultyLeadID, enrollCount))
            self.connection.commit()
            return {"message": "Section added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new objective
    def insert_objective(self, objCode, description, programName):
        try:
            self.cursor.execute("SELECT ObjCode FROM Objectives WHERE ObjCode = %s", (objCode,))
            if self.cursor.fetchone():
                return {"message": "Objective code already exists"}
            sql = "INSERT INTO Objectives (ObjCode, Description, ProgramName) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (objCode, description, programName))
            self.connection.commit()
            return {"message": "Objective added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new subobjective
    def insert_subobjective(self, subObjCode, description, objCode):
        try:
            self.cursor.execute("SELECT SubObjCode FROM SubObjectives WHERE SubObjCode = %s", (subObjCode,))
            if self.cursor.fetchone():
                return {"message": "Subobjective code already exists"}
            sql = "INSERT INTO SubObjectives (SubObjCode, Description, ObjCode) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (subObjCode, description, objCode))
            self.connection.commit()
            return {"message": "Subobjective added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to link a course to an objective
    def link_course_to_objective(self, courseID, objCode, subObjCode=None):
        try:
            self.cursor.execute("SELECT CourseObjID FROM CourseObjectives WHERE CourseID = %s AND ObjCode = %s AND (SubObjCode IS NULL OR SubObjCode = %s)", (courseID, objCode, subObjCode))
            if self.cursor.fetchone():
                return {"message": "Course-objective pair already exists"}
            sql = "INSERT INTO CourseObjectives (CourseID, ObjCode, SubObjCode) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (courseID, objCode, subObjCode))
            self.connection.commit()
            return {"message": "Course-objective pair added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to enter evaluation results for a course objective
    def insert_evaluation_result(self, courseObjID, sectionID, evalMethod, semester, year, studentsPassed):
        try:
            self.cursor.execute("SELECT ObjEvalID FROM ObjectiveEval WHERE CourseObjID = %s AND SectionID = %s AND EvalMethod = %s AND Semester = %s AND Year = %s", (courseObjID, sectionID, evalMethod, semester, year))
            if self.cursor.fetchone():
                return {"message": "Evaluation result already exists"}
            sql = "INSERT INTO ObjectiveEval (CourseObjID, SectionID, EvalMethod, Semester, Year, StudentsPassed) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseObjID, sectionID, evalMethod, semester, year, studentsPassed))
            self.connection.commit()
            return {"message": "Evaluation result added successfully"}
        except Error as e:
            return {"error": str(e)}





    