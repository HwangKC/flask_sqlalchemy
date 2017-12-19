# coding=utf-8
from flask import render_template, jsonify
from model import db, User
from config import app, listData, caseData

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html', **{'list': listData})


@app.route('/case')
def case():
    return render_template('case.html', **{'list': caseData})


@app.route('/addUser')
def add_user():
    user1 = User('admin', 'admin@qq.com')
    user2 = User('saturn', 'saturn@qq.com')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()
    db.session.close()

    return "<p>add succssfully!"


@app.route('/query/all')
def queryByAll():
    users = User.query.all()  # 查询所有数据
    if not users:
        return "<p>No users exist! <a href='/adduser'>Add users first.</a></p>"

    obj = {
        'name': '',
        'email': ''
    }
    for user in users:
        obj['name'] = user.name
        obj['email'] = user.email

    return jsonify(obj)


@app.route('/query/<name>')
def queryByName(name):
    user = User.query.filter_by(name=name).first()  # 查询数据

    if not user:
        return "<p>No user exist! <a href='/adduser'>Add user first.</a></p>"

    obj = {
        'name': user.name,
        'email': user.email
    }

    return jsonify(obj)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
