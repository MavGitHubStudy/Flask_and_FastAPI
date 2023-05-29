"""
Задание №9

Создать страницу, содержащую форму для ввода
имени и электронной почты (и кнопку "Отправить".)

При отправке которой будет создан cookie
файл с данными пользователя.

Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.

На странице приветствия должна быть кнопка "Выйти".

При нажатии на кнопку "Выйти" будет удалён
cookie файл с данными пользователя и произведено
перенаправление на страницу ввода имени
электронной почты.
"""
from markupsafe import escape
from flask import Flask, render_template, request, redirect, session, url_for


app = Flask(__name__)
app.secret_key = \
    b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    context = {
        'title': 'task_09',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_09',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_09',
    }
    return render_template('contacts.html', **context)


@app.errorhandler(400)
def bad_request(e):
    app.logger.warning(e)
    context = {
        'title': '400: Плохой запрос',
        'big_head': 'Плохой запрос',
        'error_details': 'Неверный формат ввода!',
    }
    return render_template('400.html', **context), 400


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': '404: Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404


@app.route('/email/', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        session['user_name'] = escape(request.form.get('user_name')) or 'NoName'
        session['user_email'] = escape(request.form.get('user_email')) or 'NoName'
        return redirect(url_for('welcome'))
    context = {
        'title': 'task_09',
    }
    return render_template('email.html', **context)


@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        return redirect(url_for('email'))
    context = {
        'title': 'task_09',
    }
    if 'user_name' in session:
        return render_template('welcome.html', **context)
    else:
        return redirect(url_for('email'))


@app.route('/logout/')
def logout():
    session.pop('user_name', None)
    session.pop('user_email', None)
    return redirect(url_for('email'))


if __name__ == "__main__":
    app.run(debug=True)
