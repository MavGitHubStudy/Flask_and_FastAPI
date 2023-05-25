"""
Задача №3

Написать функцию, которая будет принимать на вход два числа
и выводить на экран их сумму.
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


@app.route('/amount/<int:num1>/<int:num2>/')  # int:num - без пробела
def amount(num1, num2):
    return f"Cумма числа {num1} и числа {num2} равна: {int(num1) + int(num2)}"


if __name__ == '__main__':
    app.run(debug=True)
