# coding=utf-8
from flask import Flask, Blueprint, request, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

# test-1
app.secret_key = 'xx00'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


# test-2
class User(UserMixin):
    def is_authenticated(self):
        return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return "1"


@login_manager.user_loader
def load_user(user_id):
    user = User()
    return user


# url 重定向
auth = Blueprint('auth', __name__)


# 权限测试
@app.route('/')
@app.route('/test')
@login_required
def test():
    return render_template('admin/main.html')


# 登录
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        print('GET请求', username, password)
        return render_template('admin/login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print('POST请求', username, password)
        if username == 'admin' and password == '123456':
            user = User()
            login_user(user)
            return render_template('admin/main.html')
        return render_template('admin/login.html')


# 退出
@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('admin/login.html')


app.register_blueprint(auth, url_prefix='/auth')
app.run(debug=True)
