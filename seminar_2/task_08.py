"""
Задание №8

Создать страницу, содержащую форму для ввода
имени и кнопку "Отправить".

При нажатии на кнопку "Отправить" будет произведено
перенаправление на страницу с flash сообщением, где
будет выведено "Привет, {имя}!".
"""
from markupsafe import escape
from pathlib import Path, PurePath
from flask import Flask, flash, render_template, request, abort, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

# task_01  14:36
@app.route('/')
def index():
    context = {
        'title': 'task_08',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_08',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_08',
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
        'title': 'task_08',
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
        'title': 'task_08',
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
        'title': 'task_08',
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
        'title': 'task_08',
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
        'title': 'task_08',
    }
    return render_template('calc.html', **context)


# task_08  01:15:00 - 01:24:00
@app.route('/age/', methods=['GET', 'POST'])
def age():
    min_age = 18

    if request.method == 'POST':
        user_age = int(escape(request.form.get('user_age')))
        user_name = escape(request.form.get('user_name'))
        if user_age < min_age:
            abort(403)
        return f'Имя пользователя: {user_name}, его возраст: {user_age}'
    context = {
        'title': 'task_08',
    }
    return render_template('age.html', **context)


@app.errorhandler(403)
def not_allowed(e):
    app.logger.warning(e)
    context = {
        'title': '403: Доступ запрещён',
    }
    return render_template('403.html', **context), 403


# task_07  01:29:00 - пропустили

# task_08  01:30:00 - 01:40:00
@app.route('/flash/', methods=['GET', 'POST'])
def _flash():
    if request.method == 'POST':
        name = request.form.get('user_name')
        flash(f'Привет, {name}!')
        return redirect(url_for('_flash'))
    return render_template('flash.html')


if __name__ == "__main__":
    app.run(debug=True)
