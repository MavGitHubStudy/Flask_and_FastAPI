"""
Задача №6

Написать функцию, которая будет выводить на экран HTML страницу
с таблицей, содержащую информацию о студентах.

Таблица должна содержать следующие поля: "Имя", "Фамилия",
"Возраст", "Средний балл".

Данные о студентах должны быть переданы в шаблон через контекст.

"""
from flask import Flask, render_template

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

# Задача №5
html_templ = """
<h1>Моя первая HTML страница</h1>
 <p>Привет, мир!</p> 
"""


@app.route('/html/')
def return_html():
    return html_templ


# Задача №6
_students = [
    {
        'name': 'Иван',
        'surname': 'Иванов',
        'age': 20,
        'average_score': 5
    },
    {
        'name': 'Пётр',
        'surname': 'Петров',
        'age': 25,
        'average_score': 4
    },
    {
        'name': 'Сидор',
        'surname': 'Сидоров',
        'age': 30,
        'average_score': 3
    },
]


@app.route('/students/')
def students():
    return render_template('students.html', students=_students)


if __name__ == '__main__':
    app.run(debug=True)
