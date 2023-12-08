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
        
    # Get all tables
    def getAllDepartments(self):
        self.cursor.execute('''
            SELECT * FROM Department
        ''')
        departments = self.cursor.fetchall()
        return departments

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


    def getEvaluationResultsByCourseName(self, course_name, semester, year):
        self.cursor.execute('''
            SELECT ObjectiveEval.*
            FROM ObjectiveEval
            INNER JOIN Section ON ObjectiveEval.SecID = Section.SecID
            INNER JOIN Course ON Section.CourseID = Course.CourseID
            WHERE Course.Title = %s AND Section.Semester = %s AND Section.Year = %s
        ''', (course_name, semester, year))
        return self.cursor.fetchall()
    
    def getEvaluationResultsByAcademicYear(self, academic_year):
        self.cursor.execute('''
            SELECT ObjectiveEval.*, Objectives.ObjCode, SubObjectives.SubObjCode
            FROM ObjectiveEval
            JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
            JOIN Objectives ON CourseObjectives.ObjID = Objectives.ObjID
            LEFT JOIN SubObjectives ON Objectives.ObjID = SubObjectives.ParentObjID
            JOIN Section ON ObjectiveEval.SecID = Section.SecID
            WHERE Section.Year = %s
        ''', (academic_year,))
        return self.cursor.fetchall()
    
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
    def insert_department(self, deptId, deptName, deptCode):
        try:
            # Check if department already exists
            self.cursor.execute("SELECT DeptID FROM Department WHERE DeptName = %s OR DeptCode = %s", (deptName, deptCode))
            if self.cursor.fetchone():
                return {"message": "Department already exists"}
            # Insert new department if not exist
            sql = "INSERT INTO Department (DeptID, DeptName, DeptCode) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (deptId, deptName, deptCode))
            self.connection.commit()
            return {"message": "Department added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new faculty member
    def insert_faculty(self, name, email, deptID, position):
        try:
            #check if faculty member already exists
            self.cursor.execute("SELECT FacultyID FROM Faculty WHERE Name = %s AND Email = %s", (name, email))
            if self.cursor.fetchone():
                return {"message": "Faculty member already exists"}
            sql = "INSERT INTO Faculty (Name, Email, DeptID, Position) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (name, email, deptID, position))
            self.connection.commit()
            return {"message": "Faculty member added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new program
    def insert_program(self, progName, deptID, facultyLeadID, facultyLeadEmail):
        try:
            #check if program already exists
            self.cursor.execute("SELECT ProgID FROM Program WHERE ProgName = %s", (progName,))
            if self.cursor.fetchone():
                return {"message": "Program already exists"}  
            sql = "INSERT INTO Program (ProgName, DeptID, FacultyLeadID, FacultyLeadEmail) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (progName, deptID, facultyLeadID, facultyLeadEmail))
            self.connection.commit()
            return {"message": "Program added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}
    
    # Method to insert a new course
    def insert_course(self, courseID, title, description, deptID):
        try:
            self.cursor.execute("SELECT CourseID FROM Course WHERE CourseID = %s", (courseID,))
            if self.cursor.fetchone():
                return {"message": "Course with this ID already exists"}

            sql = "INSERT INTO Course (CourseID, DeptID, Title, Description) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (courseID, deptID, title, description))
            self.connection.commit()
            return {"message": "Course added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new section
    def insert_section(self, courseID, semester, year, facultyLeadID, enrollCount):
        try:
            self.cursor.execute("SELECT SecID FROM Section WHERE CourseID = %s AND Semester = %s AND Year = %s", (courseID, semester, year))
            if self.cursor.fetchone():
                return {"message": "Section already exists"}
            sql = "INSERT INTO Section (CourseID, Semester, Year, FacultyLeadID, EnrollCount) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseID, semester, year, facultyLeadID, enrollCount))
            self.connection.commit()
            return {"message": "Section added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new objective
    def insert_objective(self, objCode, description, deptID):
        try:
            # check if objective already exists
            self.cursor.execute("SELECT ObjID FROM Objectives WHERE ObjCode = %s", (objCode,))
            if self.cursor.fetchone():
                return {"message": "Objective already exists"}
            sql = "INSERT INTO Objectives (ObjCode, Description, DeptID) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (objCode, description, deptID))
            self.connection.commit()
            return {"message": "Objective added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to insert a new subobjective
    def insert_subobjective(self, subObjCode, description, parentObjID):
        try:
            # check if subobjective already exists
            self.cursor.execute("SELECT SubObjID FROM SubObjectives WHERE SubObjCode = %s", (subObjCode,))
            if self.cursor.fetchone():
                return {"message": "Subobjective already exists"}
            sql = "INSERT INTO SubObjectives (SubObjCode, Description, ParentObjID) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (subObjCode, description, parentObjID))
            self.connection.commit()
            return {"message": "Subobjective added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to link a course to an objective
    def link_course_to_objective(self, courseID, objID):
        try:
            self.cursor.execute("SELECT CourseObjID FROM CourseObjectives WHERE CourseID = %s AND ObjID = %s", (courseID, objID))
            if self.cursor.fetchone():
                return {"message": "Course-objective pair already exists"}
            sql = "INSERT INTO CourseObjectives (CourseID, ObjID) VALUES (%s, %s)"
            self.cursor.execute(sql, (courseID, objID))
            self.connection.commit()
            return {"message": "Course-objective pair added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to enter evaluation results for a section
    def insert_evaluation_result(self, courseObjID, secID, semester, year, evalMethod, studentsPassed):
        try:
            #check if evaluation result already exists
            self.cursor.execute("SELECT EvalID FROM ObjectiveEval WHERE CourseObjID = %s AND SecID = %s AND Semester = %s AND Year = %s AND EvalMethod = %s", (courseObjID, secID, semester, year, evalMethod))
            if self.cursor.fetchone():
                return {"message": "Evaluation result already exists"}
            sql = "INSERT INTO ObjectiveEval (CourseObjID, SecID, Semester, Year, EvalMethod, StudentsPassed) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseObjID, secID, semester, year, evalMethod, studentsPassed))
            self.connection.commit()
            return {"message": "Evaluation result added successfully"}  
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}
        
    # Method to link a course to a program
    def link_course_to_program(self, ProgID, courseID):
        try:
            self.cursor.execute("SELECT ProgramCourseID FROM ProgramCourses WHERE ProgID = %s AND CourseID = %s", (ProgID, courseID))
            if self.cursor.fetchone():
                return {"message": "Course-program pair already exists"}
            sql = "INSERT INTO ProgramCourses (ProgID, CourseID) VALUES (%s, %s)"
            self.cursor.execute(sql, (ProgID, courseID))
            self.connection.commit()
            return {"message": "Course-program pair added successfully"}
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}

    # Method to assign an objective to a course-program pair
    def assign_objective_to_course_program(self, ProgID, courseID, objID):
        try:
            # First, find the ProgramCourseID from ProgramCourses table
            self.cursor.execute("SELECT ProgramCourseID FROM ProgramCourses WHERE ProgID = %s AND CourseID = %s", (ProgID, courseID))
            program_course_entry = self.cursor.fetchone()
            if not program_course_entry:
                return {"message": "No matching program-course pair found"}

            program_course_id = program_course_entry[0]

            # check if course-program-objective pair already exists
            self.cursor.execute("SELECT CourseProgObjID FROM CourseProgramObjectives WHERE ProgramCourseID = %s AND ObjID = %s", (program_course_id, objID))
            if self.cursor.fetchone():
                return {"message": "Course-program-objective pair already exists"}

            sql = "INSERT INTO CourseProgramObjectives (ProgramCourseID, ObjID) VALUES (%s, %s)"
            self.cursor.execute(sql, (program_course_id, objID))
            self.connection.commit()
            return {"message": "Course-program-objective pair added successfully"}  
        except mysql.connector.errors.IntegrityError as e:
            return {"error": str(e)}



    