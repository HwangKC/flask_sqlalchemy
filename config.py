# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/py_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

listData = [{
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