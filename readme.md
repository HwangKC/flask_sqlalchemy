## Python App

> pip list --format=columns

<pre>
Package          Version
---------------- -------
click            6.7
Flask            0.12.2
Flask-SQLAlchemy 2.3.2
itsdangerous     0.24
Jinja2           2.10
MarkupSafe       1.0
pip              9.0.1
setuptools       28.8.0
SQLAlchemy       1.1.15
Werkzeug         0.13
</pre>

- Windows系统没这个还真没法玩
> MySQL_python-1.2.5-cp27-none-win_amd64.whl

> https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python


- 安装或升级包后，更新依赖记录：

> pip freeze > requirements.txt


- 当需要导入，安装各种包时：
> pip install -r requirements.txt