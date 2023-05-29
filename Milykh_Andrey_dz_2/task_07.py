"""
Задание №7

Создать страницу, содержащую форму для ввода
числа и кнопку "Отправить".

При нажатии на кнопку "Отправить" будет произведено
перенаправление на страницу с результатом, где будет
выведено введённое число и его квадрат.
"""
from html import escape
from flask import Flask, render_template, request, abort


app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'task_07',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_07',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_07',
    }
    return render_template('contacts.html', **context)


@app.route('/square/', methods=['GET', 'POST'])
def square():
    context = {
        'title': 'task_07',
        'url': 'square',
    }
    if request.method == 'POST':
        try:
            number = float(escape(request.form.get('number')))
            return f'Квадрат числа {number} равен {number * number}'
        except ValueError:
            abort(400)
    return render_template('square.html', **context)


@app.errorhandler(400)
def bad_request(e):
    app.logger.warning(e)
    context = {
        'title': '400: Плохой запрос',
        'big_head': 'Плохой запрос',
        'error_details': 'Неверный формат ввода!'
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


if __name__ == "__main__":
    app.run(debug=True)
