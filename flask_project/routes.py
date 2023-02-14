from flask_project import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from flask_project.forms import RegistrationForm, LoginForm, ConnectionForm
from flask_project.models import User, Host
from flask_login import login_user, logout_user, current_user, login_required
import psycopg2
from sqlalchemy.exc import IntegrityError
from flask_project.ssh import connect

try: 
    conn = psycopg2.connect(database="flaskapp", user="roger",  
    password="1234", host="localhost")
    mycursor = conn.cursor()
except:
    print ("I am unable to connect to the database")

@app.route('/')
def homepage():
    return render_template('homepage.html',title='Home Page')

@app.route('/server',methods=['POST','GET'])
@login_required
def server():
    form = ConnectionForm()
    if form.validate_on_submit():
        host_input=Host.query.filter_by(host=form.host.data, user=form.user.data).first()
        # print(host_input)
        if host_input:
            flash(f'Server and User exists!', category='danger')
        else:
            host=Host(host=form.host.data,user=form.user.data)
            db.session.add(host)
            db.session.commit()
            flash(f'Server added successfully!', category='success')
    mycursor.execute('Select * from host')
    data = mycursor.fetchall()
    return render_template('server.html',title='Server',form=form, data=data)

@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('server'))
    form = RegistrationForm()
    if form.validate_on_submit():
        encrypt=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=encrypt)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully!', category='success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            # Don't stop the stream, just ignore the duplicate.
            flash(f'User account exists!', category='danger')
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('server'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'{form.username.data} Login Success!', category='success')
            return redirect(url_for('server'))
        else:
            flash(f'Login fail', category='danger')
    return render_template('login.html',title='Login',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/process/host=<string:host>&user=<string:user>', methods=['POST','GET'])
def process(host,user):
    data = connect(host, user)
    return render_template('process.html',title='Process', data=data)