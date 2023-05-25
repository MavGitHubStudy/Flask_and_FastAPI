"""
Задача №5

Написать функцию, которая будет выводить на экран HTML страницу
с заголовком "Моя первая HTML страница" и абзацем "Привет, мир!".
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


@app.route('/string/<line>/')
def string(line):
    return f'{len(line)}'


html_templ = """
<h1>Моя первая HTML страница</h1>
 <p>Привет, мир!</p> 
"""


@app.route('/html/')
def return_html():
    return html_templ


if __name__ == '__main__':
    app.run(debug=True)
