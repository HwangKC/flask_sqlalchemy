# coding=utf-8
from flask import Flask, render_template, jsonify
from app import User, db

app = Flask(__name__)

data_index = [{
    'title': '控制器',
    'info': '极致外形，超长续航',
    'pic': 'yunzi@2x.png',
}, {
    'title': '控制器',
    'info': 'USB接口供电，有电环境大规模部署',
    'pic': 'yunbiao@2x.png',
}, {
    'title': '控制器',
    'info': '安装4AA电池，可循环利用成本更低',
    'pic': 'station@2x.png',
}, {
    'title': '控制器',
    'info': '增加防水保护，适用场景更广泛',
    'pic': 'yunhe-pro@2x.png',
}, {
    'title': '控制器',
    'info': '十公里覆盖，远距离超低成本',
    'pic': 'chip@2x.png',
}, {
    'title': '控制器',
    'info': '精致小巧，感知远近',
    'pic': 'sensoro-4aa@2x.png',
}]


@app.route('/')
def index():
    user = User.query.filter_by(name='saturn').first()
    return render_template('index.html', **{'list': data_index, 'title': user})


@app.route('/case')
def case():
    return render_template('case.html', **{'list': data_index})


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
    user = User.query.filter_by(name=name).first() # 查询数据

    if not user:
        return "<p>No user exist! <a href='/adduser'>Add user first.</a></p>"

    obj = {
        'name': '',
        'email': ''
    }
    obj['name'] = user.name
    obj['email'] = user.email

    return jsonify(obj)


if __name__ == '__main__':
    app.run(debug=True)
