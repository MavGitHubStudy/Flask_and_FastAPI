"""
Задание №2

Создать базу данных для хранения информации о книгах в библиотеке.

База данных должна содержать две таблицы: "Книги" и "Авторы".

В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.

В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.

Необходимо создать связь между таблицами "Книги" и "Авторы".

Написать функцию-обработчик, которая будет выводить список всех
книг с указанием их авторов.
"""
import random
from flask import Flask, render_template

from Milykh_Andrey_dz_3.models_02 import db, Author, Book

app = Flask(__name__)
# Подсоединение к базе данных
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/library.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# Для команды в терминале >>> flask init-db
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK - создали БД library.db')


@app.cli.command("fill-db")
def fill_db():
    count = 10
    # Добавляем авторов
    for author in range(1, count + 1):
        new_author = Author(first_name=f'FirstName{author}',
                            last_name=f'LastName{author}')
        db.session.add(new_author)
    db.session.commit()

    # Добавляем книги
    for book in range(1, count ** 2):
        new_book = Book(title=f'Title{book}',
                        year_pub=random.randint(1950, 2023),
                        quantity=random.randint(1, 10),
                        author_id=random.randint(1, count + 1))
        db.session.add(new_book)
    db.session.commit()
    print('База "library.db" заполнена!')


@app.route('/')
def index():
    context = {
        'title': 'task_02',
    }
    return render_template('index.html', **context)


@app.route('/books/')
def all_books():
    books = Book.query.all()
    context = {
        'title': 'task_02',
        'books': books}
    return render_template('books.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_02',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_02',
    }
    return render_template('contacts.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
