
import os
from flask_bcrypt import Bcrypt
from app import app, db, Instructor

bcrypt = Bcrypt()

# Absolute DB path setup
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'studentregistration.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

with app.app_context():
    instructors = Instructor.query.all()
    updated = 0
    for instructor in instructors:
        if not instructor.Password_Hash:
            raw_password = f"password{instructor.InstructorID}"
            instructor.Password_Hash = bcrypt.generate_password_hash(raw_password).decode('utf-8')
            print(f"✅ Set password for {instructor.InstructorID}: {raw_password}")
            updated += 1
    db.session.commit()
    print(f"✅ Done. {updated} instructors updated.")
