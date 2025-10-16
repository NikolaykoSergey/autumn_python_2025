from xml.sax.saxutils import escape

from flask import Flask
from flask import request
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     # return "<p>Hello, World!</p>"
#     name = request.args.get("promt", "")
#     clid = request.args.get("clid", "ID")
#     return f"Hello, {escape(name)}! Hello, {escape(clid)}!"
#
#
# @app.route("/about")
# def page_about():
#     return "<html><p>Немного о себе</p><html>"

# @app.route("/contacts")
#     return "<html> Конакты <html>"

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/posts')
def posts():
    posts_list = [
        'Пост 1: Введение во Flask',
        'Пост 2: Работа с Docker desktop',
        'Пост 3: Настройка маршрутов и форм'
    ]
    return render_template('posts.html', posts=posts_list)

if __name__ == '__main__':
    app.run(debug=True)