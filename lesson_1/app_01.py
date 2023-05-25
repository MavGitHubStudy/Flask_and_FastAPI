from flask import Flask  # стандартное начало

app = Flask(__name__)  # app - классическое имя для проекта


@app.route('/')  # есть адрес, по которому мы можем зайти
def hello_world():
    return 'Hello World!'
    # return 42


if __name__ == '__main__':
    app.run()  # запуск сервера
