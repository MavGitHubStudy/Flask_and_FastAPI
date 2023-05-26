"""
Задание №3

Создать страницу, содержащую форму для ввода
логина и пароля.
При нажатии на кнопку "Отправить" будет произведена
проверка соответсвия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""
from pathlib import Path, PurePath
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


# task_01  14:36
@app.route('/')
def index():
    context = {
        'title': 'task_03',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_03',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_03',
    }
    return render_template('contacts.html', **context)


@app.route('/hello/')
def hello():
    name = 'Bob'
    return f'Hello, {name}!'


# task_02  29:00
@app.route('/img_upload/')
def img_upload():
    context = {
        'title': 'task_03',
    }
    return render_template('img_upload.html', **context)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    context = {
        'title': 'task_03',
    }
    return render_template('upload.html', **context)


# task_03  45:00 - 50:30 - 56:16
users = ['John', 'Olga', 'Smith']
info = {
    'John': '123',
    'Olga': 'qwerty',
    'Smith': '12345',
}


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and password == info[username]:
            return f"Hello,  {username}!"
    context = {
        'title': 'task_03',
    }
    return render_template('login.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
