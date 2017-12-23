# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# CREATE TABLE eis_user(
#   id         INT(11)  Not Null  AUTO_INCREMENT PRIMARY KEY,
#   cname      VARCHAR(255) NULL
#   ename      VARCHAR(255) NULL
#   password   VARCHAR(255) NULL
#   is_admin   BIT       NULL
#   company_id VARCHAR(255) NULL
#   enabled    BIT       NULL
# );

class User(db.Model):
    __tablename__ = 'eis_user'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(255), unique=True)
    ename = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    is_admin = db.Column(db.Integer, unique=True)
    company_id = db.Column(db.String(255), unique=True)
    enabled = db.Column(db.Integer, unique=True)

    def __init__(self, cname, ename, password, is_admin, company_id, enabled):
        self.cname = cname
        self.ename = ename
        self.password = password
        self.is_admin = is_admin
        self.company_id = company_id
        self.enabled = enabled


# CREATE TABLE eis_company(
#   id     INT(11)  Not Null  AUTO_INCREMENT PRIMARY KEY,
#   name   VARCHAR(255)  NULL
#   desc   VARCHAR(1024) NULL
# );

# class Company(db.Model):
#     __tablename__ = 'eis_company'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), unicode=True)
#     desc = db.Column(db.String(1024), unicode=True)
