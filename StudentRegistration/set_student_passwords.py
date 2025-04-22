
import os
from flask_bcrypt import Bcrypt
from app import app, db, Student

bcrypt = Bcrypt()

# Ensure proper DB path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'studentregistration.db')

with app.app_context():
    students = Student.query.all()
    updated = 0
    for student in students:
        if not student.Password_Hash:
            password = f"password{student.StudentID}"
            student.Password_Hash = bcrypt.generate_password_hash(password).decode('utf-8')
            print(f"✅ Set password for {student.StudentID}: {password}")
            updated += 1
    db.session.commit()
    print(f"✅ Done. {updated} students updated.")
