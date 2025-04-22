from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Use SQLite for demo; update URI if you're using MySQL/PostgreSQL
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'studentregistration.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# =======================
# Database Models
# =======================
class Department(db.Model):
    __tablename__ = 'department'
    DepartmentID = db.Column(db.Integer, primary_key=True)
    Department_Name = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    __tablename__ = 'course'
    CourseID = db.Column(db.Integer, primary_key=True)
    Course_Name = db.Column(db.String(150), nullable=False)
    Credits = db.Column(db.Integer, nullable=False)
    DepartmentID = db.Column(db.Integer, db.ForeignKey('department.DepartmentID'))
    Class_Time = db.Column(db.String(50))
    Days = db.Column(db.String(20))
    is_synchronous = db.Column(db.Boolean)

class Student(db.Model):
    __tablename__ = 'student'
    StudentID = db.Column(db.Integer, primary_key=True)
    S_First_Name = db.Column(db.String(45), nullable=False)
    S_Last_Name = db.Column(db.String(45), nullable=False)
    S_Email = db.Column(db.String(255), nullable=False)
    Year = db.Column(db.Integer, nullable=False)
    Major = db.Column(db.String(255), nullable=False)
    Class1 = db.Column(db.String(100), nullable=False)
    Class2 = db.Column(db.String(100), nullable=False)
    Class3 = db.Column(db.String(100), nullable=False)
    Password_Hash = db.Column(db.String(255))

class Instructor(db.Model):
    __tablename__ = 'instructor'
    InstructorID = db.Column(db.Integer, primary_key=True)
    I_First_Name = db.Column(db.String(100), nullable=False)
    I_Last_Name = db.Column(db.String(100), nullable=False)
    DepartmentID = db.Column(db.Integer, db.ForeignKey('department.DepartmentID'), nullable=False)
    CourseName = db.Column(db.String(100), nullable=False)
    Semester = db.Column(db.String(20), nullable=False)
    Password_Hash = db.Column(db.String(255))

class Session(db.Model):
    __tablename__ = 'session'
    SessionID = db.Column(db.Integer, primary_key=True)
    CourseID = db.Column(db.Integer, db.ForeignKey('course.CourseID'), nullable=False)
    InstructorID = db.Column(db.Integer, db.ForeignKey('instructor.InstructorID'), nullable=False)
    Max_Students = db.Column(db.Integer, nullable=False)

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    EnrollmentID = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, db.ForeignKey('student.StudentID'), nullable=False)
    SessionID = db.Column(db.Integer, db.ForeignKey('session.SessionID'), nullable=False)
    Enrollment_Date = db.Column(db.String(10), nullable=False)

class StudentBalances(db.Model):
    __tablename__ = 'studentbalances'
    StudentBalanceID = db.Column(db.Integer, primary_key=True)
    Balance = db.Column(db.Numeric(15, 2), nullable=False)
    StudentID = db.Column(db.Integer, db.ForeignKey('student.StudentID'), nullable=False)
    S_First_Name = db.Column(db.String(45), nullable=False)
    S_Last_Name = db.Column(db.String(45), nullable=False)

class StudentNotifications(db.Model):
    __tablename__ = 'studentnotifications'
    notification_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.StudentID'))
    student_name = db.Column(db.String(100))
    notification_type = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(30))

# =======================
# Routes
# =======================

@app.route('/')
def portal():
    return render_template('loginportal.html')

@app.route('/student-login')
def student_login():
    return render_template('studentlogin.html')

@app.route('/login-instructor', methods=['GET', 'POST'])
def login_instructor():
    if request.method == 'POST':
        instructor_id = request.form['instructor_id']
        password = request.form['password']
        instructor = Instructor.query.filter_by(InstructorID=instructor_id).first()
        if instructor and bcrypt.check_password_hash(instructor.Password_Hash, password):
            session['instructor_id'] = instructor.InstructorID
            return redirect(url_for('instructor_courses'))
        return "Invalid instructor login"
    
    # If GET request, show the form
    return render_template('instructorlogin.html')

@app.route('/student-login', methods=['POST'])
def handle_student_login():
    student_id = request.form['student_id']
    password = request.form['password']
    student = Student.query.filter_by(StudentID=student_id).first()
    if student and bcrypt.check_password_hash(student.Password_Hash, password):
        session['student_id'] = student.StudentID
        return redirect(url_for('student_homepage'))
    return "Invalid student login"

@app.route('/logout')
def logout():
    session.clear()  # Clears all session data
    return redirect(url_for('portal'))  # Or redirect to 'student_login' or another page

@app.route('/student-homepage')
def student_homepage():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))
    student = Student.query.get(session['student_id'])
    return render_template('studenthomepage.html', student=student)

@app.route('/student-degree')
def student_degree():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))
    student = Student.query.get(session['student_id'])
    return render_template('studentdegree.html', student=student)

@app.route('/register-courses')
def register_courses():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))
    sessions = db.session.query(Session, Course).join(Course).all()
    return render_template('register_courses.html', sessions=sessions)

@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    if 'student_id' not in session:
        return redirect(url_for('student_login'))
    session_id = request.form['session_id']
    student_id = session['student_id']
    existing = Enrollment.query.filter_by(StudentID=student_id, SessionID=session_id).first()
    if existing:
        return "Already enrolled."
    enrollment = Enrollment(
        EnrollmentID=random.randint(100000, 999999),
        StudentID=student_id,
        SessionID=session_id,
        Enrollment_Date=datetime.now().strftime("%m-%d-%Y")
    )
    db.session.add(enrollment)
    db.session.commit()
    return "Enrolled successfully!"

@app.route('/instructor-courses')
def instructor_courses():
    if 'instructor_id' not in session:
        return redirect(url_for('instructor_login'))

    instructor_id = session['instructor_id']
    sessions = (
        db.session.query(Session, Course)
        .join(Course, Session.CourseID == Course.CourseID)
        .filter(Session.InstructorID == instructor_id)
        .all()
    )

    instructor = Instructor.query.get(instructor_id)
    return render_template('instructor_courses.html', instructor=instructor, sessions=sessions)


# =======================
# Initialize DB
# =======================
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
