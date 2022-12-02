from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username required."),  
        Length(min=4, max=25, message="Username must be between 4 and 25 characters.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password required."), 
        Length(min=8, message="")])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    signUp = SubmitField('Sign Up')
    
