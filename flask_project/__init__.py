from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/flask.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://roger:1234@localhost:5432/flaskapp'

db=SQLAlchemy(app,session_options={'autoflush':False})
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

# from flask_project.models import Host, User
# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     db.session.commit()
    
from flask_project import routes