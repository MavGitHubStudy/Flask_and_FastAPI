"""
Задание №1

Создать страницу, содержащую кнопку "Нажми меня",
при нажатии на которую будет переход на другую страницу
с приветствием пользователя по имени.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'task_01',
    }
    return render_template('index.html', **context)


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
