from flask import Flask, request, flash, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from forms_05 import RegistrationForm, LoginForm
from models_05 import db, User

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SECRET_KEY'] = b'2bc64352e8d6be54e518a6731e4a9e8330eee6130559ed5fb6c779bab3f88e3d'
csrf = CSRFProtect(app)
"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""

# Подсоединение к базе данных
print(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_05.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/task_05.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def index():
    context = {
        'title': 'task_05',
    }
    return render_template('index.html', **context)


@app.route('/about/')
def about():
    context = {
        'title': 'task_05',
    }
    return render_template('about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {
        'title': 'task_05',
    }
    return render_template('contacts.html', **context)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        result = db.session.query(User).filter(User.email == email)
        for row in result:
            if check_password_hash(row.password, password):
                flash("Login successful", "success")
                context = {
                    'title': 'task_05',
                }
                return render_template('success.html', **context)
            else:
                return redirect('/login/')

    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data

        print(firstname, lastname, email, password)
        psw_hash = generate_password_hash(password)
        print(firstname, lastname, email, psw_hash)

        new_user = User(firstname=firstname, lastname=lastname, email=email, password=psw_hash)
        print(new_user)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(f"Вы успешно зарегистрированы", "success")
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            return "Ошибка записи в БД!"

    return render_template('register.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
