"""
Задание №1

Создать базу данных для хранения информации о студентах университета.

База данных должна содержать две таблицы: "Студенты" и "Факультеты".

В таблице "Студенты" должны быть следующие поля: id, имя, фамилия,
возраст, пол, группа и id факультета.

В таблице "Факультеты" должны быть следующие поля: id и название
факультета.

Необходимо создать связь между таблицами "Студенты" и "Факультеты".

Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их факультета.
"""
import random
from flask import Flask, render_template
from seminar_3.models_01 import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/university.db'
db.init_app(app)


# Для команды в терминале >>> flask init-db
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK - создали БД')


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    # Добавляем факультеты
    for faculty in range(1, count + 1):
        new_faculty = Faculty(title=f'Faculty{faculty}')
        db.session.add(new_faculty)
    db.session.commit()

    # Добавляем студентов
    gender_lst = ['f', 'm']
    for student in range(1, count ** 2):
        new_student = Student(first_name=f'FirstName{student}',
                              last_name=f'LastName{student}',
                              age=random.randint(18, 45),
                              gender=random.choice(gender_lst),
                              group=f'Group{random.randint(1, 3)}',
                              faculty_id=random.randint(1, 5)
                              )
        db.session.add(new_student)
    db.session.commit()


@app.route('/')
def index():
    context = {
        'title': 'task_01',
    }
    return render_template('index.html', **context)


@app.route('/students/')
def all_students():
    students = Student.query.all()
    context = {
        'title': 'task_01',
        'students': students}
    return render_template('students.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_01',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_01',
    }
    return render_template('contacts.html', **context)


@app.route('/hello/')
def hello():
    name = 'Bob'
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run(debug=True)
