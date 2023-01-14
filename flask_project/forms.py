#This form shows the info about user info and IP info
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields import EmailField

#Form for user sign up
class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(),validators.Length(3,20)])
    email = EmailField('Email', [validators.DataRequired(),validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(),validators.Length(6,16)])
    confirm_password = PasswordField('Confirm Password', [validators.DataRequired(),validators.EqualTo('password',message='Passwords must match')])
    submit = SubmitField(label='Sign up')

#Form for user login
class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired(),validators.Length(3,20)])
    '''email = EmailField('Email', [validators.DataRequired(),validators.Email()])'''
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(6,16)])
    submit = SubmitField(label='Login')

#Form for connection
class ConnectionForm(FlaskForm):
    host = StringField('IP Address', [validators.IPAddress()])
    user = StringField('User')
    add = SubmitField(label='Add')