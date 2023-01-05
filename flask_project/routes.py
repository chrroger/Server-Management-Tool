from flask_project import app
from flask import render_template, redirect, url_for, flash
from flask_project.forms import RegistrationForm, LoginForm


@app.route('/')
def homepage():
    return render_template('homepage.html',title='Home Page')

@app.route('/server')
def server():
    return render_template('server.html',title='Server')

@app.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if True: #need modify after adding database
            flash(f'{form.username.data} Login Success!', category='success')
            return redirect(url_for('server'))
        else:
            flash(f'Login fail', category='danger')
    return render_template('login.html',title='Login',form=form)
