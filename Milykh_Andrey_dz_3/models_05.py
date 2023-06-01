from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return f'User({self.email})'

    def __str__(self):
        return (
            f"Имя: {self.firstname}\n"
            f"Фамилия: {self.lastname}\n"
            f"Электронная почта: {self.email}\n"
            f"Пароль: {self.password}"
        )
