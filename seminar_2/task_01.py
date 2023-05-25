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
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/hello/')
def hello():
    name = 'Bob'
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run(debug=True)
