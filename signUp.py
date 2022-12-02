from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from config import User


# def invalid_credentials(form, field):
#     username_entered = form.username.data
#     password_entered = field.data

#     user_object = User.query.filter_by(username=username_entered).first()
#     if user_object is None:
#         raise ValidationError("Username already exists. Select a different username. ")


class signUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username required."),  
        Length(min=4, max=25, message="Username must be between 4 and 25 characters.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password required."), 
        Length(min=8, message="Password must be more than 8 characters long")])
    confirm_password = PasswordField('Password', validators=[DataRequired(message="Password required."), 
        EqualTo('password', message='Password must match.')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is taken. Please choose another.')
    