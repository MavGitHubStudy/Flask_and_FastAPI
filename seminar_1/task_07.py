"""
Задача №7

Написать функцию, которая будет выводить на экран HTML страницу
с блоками новостей.

Каждый блок должен содержать заголовок новости, краткое
описание и дату публикации.

Данные о новостях должны быть переданы в шаблон через контекст.

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


# Задача №7

_news = [
    {
        'title': 'Новость1',
        'description': 'Содержимое новости 1',
        'date': '18.05.2023'
    },
    {
        'title': 'Новость2',
        'description': 'Содержимое новости 2',
        'date': '19.05.2023'
    },
    {
        'title': 'Новость3',
        'description': 'Содержимое новости 3',
        'date': '22.05.2023'
    },
]


@app.route('/news/')
def news():
    return render_template('news.html', news=_news)


if __name__ == '__main__':
    app.run(debug=True)
