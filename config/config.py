# -*- coding: utf-8 -*-
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'py_db'

SECRET_KEY = 'secret_key'
DEBUG = True

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
