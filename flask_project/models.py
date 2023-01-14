#This model stores the data from database
from flask_project import db, login_manager
from flask_login import UserMixin
from flask import redirect, url_for

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('homepage'))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True,nullable=False)
    email=db.Column(db.String(120), unique=True,nullable=False)
    password=db.Column(db.String(60),nullable=False)
    date=db.Column(db.DateTime, default=db.func.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.date}'
        
class Host(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    host=db.Column(db.String(20), nullable=False)
    user=db.Column(db.String(20), nullable=False)
    date=db.Column(db.DateTime, default=db.func.now())

    def __init__(self, host, user):
        self.host = host
        self.user = user

    def __repr__(self):
        return f'{self.host}:{self.user}:{self.date}'
