"""
Задача №2

Дорабатываем задачу №1.
Добавьте дополнительные страницы в наше веб-приложение:
страницу "about"
страницу "contact"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def contact():
    return 'Contact'


if __name__ == '__main__':
    app.run(debug=True)
