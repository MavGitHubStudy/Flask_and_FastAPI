"""
Задание №2

Создать страницу, содержащую изображение и ссылку
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Первая страница'


if __name__ == "__main__":
    app.run(debug=True)
