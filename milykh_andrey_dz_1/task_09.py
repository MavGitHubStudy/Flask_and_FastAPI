"""
Задача №9

Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.

Например, создать страницы "Одежда", "Обувь"
и "Куртка", используя базовый шаблон.
"""
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Подсоединение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'shop.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# БД - Таблицы - Записи
# Таблица:
# id    title   price   isActive
# 1     Some    100     True
# 2     Some2   200     False
# 3     Some3   40      True


# Одежда
class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


# Обувь
class Shoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    # text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


@app.route('/')
@app.route('/clothes/')
def index():
    items_clothes = Clothes.query.order_by(Clothes.price).all()
    return render_template('index_shop.html', data=items_clothes)


@app.route('/shoes/')
def shoes():
    items_shoes = Shoes.query.order_by(Shoes.price).all()
    return render_template('shoes_shop.html', data=items_shoes)


@app.route('/about/')
def about():
    return render_template('about_shop.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts_shop.html')


@app.route('/create_clothes/', methods=['POST', 'GET'])
def create_clothes():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']

        item_clothes = Clothes(title=title, price=price)
        try:
            db.session.add(item_clothes)
            db.session.commit()
            return redirect('/clothes/')
        except IntegrityError:
            db.session.rollback()
            return "Получилась ошибка записи в БД"
    else:
        return render_template('create_clothes.html')


@app.route('/create_shoes/', methods=['POST', 'GET'])
def create_shoes():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']

        item_shoes = Shoes(title=title, price=price)
        try:
            db.session.add(item_shoes)
            db.session.commit()
            return redirect('/shoes/')
        except IntegrityError:
            db.session.rollback()
            return "Получилась ошибка записи в БД"
    else:
        return render_template('create_shoes.html')


if __name__ == '__main__':
    app.run(debug=True)
