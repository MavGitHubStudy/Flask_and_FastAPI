from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.String(80), unique=False, nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),
                           nullable=False)

    def __repr__(self):
        return f'Student({self.first_name}, {self.last_name})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    students = db.relationship('Student', backref='faculty')

    def __repr__(self):
        return f'Faculty({self.title})'
