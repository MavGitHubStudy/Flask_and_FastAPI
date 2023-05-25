"""
Задание №2

Создать страницу, содержащую изображение и ссылку
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from pathlib import Path, PurePath
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'task_02',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_02',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_02',
    }
    return render_template('contacts.html', **context)


@app.route('/hello/')
def hello():
    name = 'Bob'
    return f'Hello, {name}!'


@app.route('/img_upload/')
def img_upload():
    context = {
        'title': 'task_02',
    }
    return render_template('img_upload.html', **context)


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f"Файл {file_name} загружен на сервер"
    context = {
        'title': 'task_02',
    }
    return render_template('upload.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
