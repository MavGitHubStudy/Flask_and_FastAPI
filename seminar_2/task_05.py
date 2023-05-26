"""
Задание №5

Создать страницу, содержащую форму для ввода двух
чисел и выбор операции(сложение, вычитание, умножение
или деление) и кнопку "Вычислить".

При нажатии на кнопку "Вычислить" будет произведено
вычисление результата выбранной операции и переход
на страницу с результатом.
"""
from html import escape
from pathlib import Path, PurePath
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


# task_01  14:36
@app.route('/')
def index():
    context = {
        'title': 'task_05',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_05',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_05',
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
        'title': 'task_05',
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
        'title': 'task_05',
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
        'title': 'task_05',
    }
    return render_template('login.html', **context)


# task_04  58:00 - 01:01:00
@app.route('/send_text/', methods=['GET', 'POST'])
def send_text():
    if request.method == 'POST':
        text = escape(request.form.get('text'))
        s = " ".join(text.split())
        return f"количество слов: {len(s.split(' '))}!"
    context = {
        'title': 'task_05',
    }
    return render_template('text.html', **context)


# task_05  01:04:20 - 01:12:30
@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        number1 = float(escape(request.form.get('number1')))
        number2 = float(escape(request.form.get('number2')))
        operation = escape(request.form.get('operations'))
        if operation == '+':
            return f'Сумма: {number1 + number2}'
        if operation == '-':
            return f'Разность: {number1 - number2}'
        if operation == '*':
            return f'Произведение: {number1 * number2}'
        if operation == '/':
            return f'Частное: {number1 / number2}'
    context = {
        'title': 'task_05',
    }
    return render_template('calc.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
