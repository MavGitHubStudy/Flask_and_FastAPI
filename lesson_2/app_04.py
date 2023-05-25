"""
Обработка GET запросов
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/get/')
def get():
    # args - это неизменяемый словарь
    if level := request.args.get('level'):
        text = f'Похоже, ты опытный игрок, раз имеешь уровень {level}<br>'
    else:  # none
        text = 'Привет, новичок.<br>'
    return f'{text} {request.args}'


if __name__ == "__main__":
    app.run(debug=True)
"""
http://localhost:5000/get/?name=alex&age=13&level=80

Похоже, ты опытный игрок, раз имеешь уровень 80
ImmutableMultiDict([('name', 'alex'), ('age', '13'), ('level', '80')])
"""