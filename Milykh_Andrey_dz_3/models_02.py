from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year_pub = db.Column(db.Integer, unique=False, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'),
                          nullable=False)

    def __repr__(self):
        return f'Book({self.title}, {self.year_pub})'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'Author({self.first_name}, {self.last_name})'
