from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from mysql_db import MySQL
import mysql.connector as connector

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

mysql = MySQL(app)

CREATE_PARAMS = ['login', 'password', 'first_name', 'last_name', 'middle_name', 'role_id']
UPDATE_PARAMS = ['first_name', 'last_name', 'middle_name', 'role_id']

from auth import init_login_manager, bp as auth_bp, check_rights
from visits import bp as visits_bp

init_login_manager(app)
app.register_blueprint(auth_bp)
app.register_blueprint(visits_bp)

@app.before_request
def log_visit_info():
    if request.endpoint == 'static':
        return None
    user_id = getattr(current_user, 'id', None)
    request.path
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(
                ('INSERT INTO visit_logs (user_id, path) VALUES (%s, %s)'),
                (user_id, request.path))
            mysql.connection.commit()
        except:
            pass

def request_params(params_list):
    params = {}
    for param_name in params_list:
        params[param_name] = request.form.get(param_name) or None
    return params

def load_roles():
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT id, name FROM roles;')
        roles = cursor.fetchall()
    return roles
class User(UserMixin):
    def __init__(self, user_id, login):
        super().__init__()
        self.id = user_id
        self.login = login


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT users.*, roles.name AS role_name FROM users LEFT OUTER JOIN roles ON users.role_id = roles.id;')
        users = cursor.fetchall()
    return render_template('users/index.html', users=users)

@app.route('/users/new')
@login_required
@check_rights('create')
def new():
    return render_template('users/new.html', user={}, roles=load_roles())

@app.route('/users/create', methods=['POST'])
@login_required
@check_rights('create')
def create():
    params = request_params(CREATE_PARAMS)
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(
                ('INSERT INTO users (login, password_hash, first_name, last_name, middle_name, role_id)'
                'VALUES(%(login)s, SHA2(%(password)s, 256), %(first_name)s, %(last_name)s, %(middle_name)s, %(role_id)s);'),
                params
            )
            mysql.connection.commit()
        except connector.Error:
            mysql.connection.rollback()
            flash('?????????????? ???????????????????????? ????????????. ???????????? ????????????????????', 'danger')
            return render_template('users/new.html', user=params, roles=load_roles())
    flash(f"???????????????????????? {params.get('login')} ?????? ?????????????? ????????????", 'success')
    return redirect(url_for('users'))

@app.route('/users/<int:user_id>')
@login_required
def show(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
        user = cursor.fetchone()
    return render_template('users/show.html', user=user)

@app.route('/users/<int:user_id>/edit')
@login_required
@check_rights('update')
def edit(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
        user = cursor.fetchone()
    return render_template('users/edit.html', user=user, roles=load_roles())

@app.route('/users/<int:user_id>/update', methods=['POST', 'GET'])
@login_required
@check_rights('update')
def update(user_id):
    params = request_params(UPDATE_PARAMS)
    params['id'] = user_id
    if not current_user.can('assign_role'):
        del params['role_id']
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute(
                (f"UPDATE users SET {','.join(['{0}=%({0})s'.format(k) for k, v in params.items() if k != 'id'])}"  
                'WHERE id = %(id)s;'),
                params
            )
            mysql.connection.commit()
        except connector.Error:
            mysql.connection.rollback()
            flash('?????????????? ???????????????????????? ????????????. ???????????? ????????????????????', 'danger')
            return render_template('users/edit.html', user=params, roles=load_roles())
    flash("???????????????????????? ?????? ?????????????? ????????????????", 'success')
    return redirect(url_for('show', user_id=user_id))

@app.route('/users/<int:user_id>/delete', methods=['POST', 'GET'])
@login_required
@check_rights('delete')
def delete(user_id):
    with mysql.connection.cursor(named_tuple=True) as cursor:
        try:
            cursor.execute('DELETE FROM users WHERE id = %s;', (user_id,))
            mysql.connection.commit()
        except connector.Error:
            mysql.connection.rollback()
            flash('?????? ???????????????? ?????????????????? ????????????', 'danger')
            return redirect(url_for('users'))
    flash("???????????????????????? ?????? ?????????????? ????????????", 'success')
    return redirect(url_for('users'))