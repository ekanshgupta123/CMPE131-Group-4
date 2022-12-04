from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_wtf.file import FileField
from config import User
import re
from wtforms.widgets import TextArea

def invalid_credentials(form, field):
    username_entered = form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None:
        raise ValidationError("Username or password is incorrect. ")
    elif password_entered != user_object.password:
        raise ValidationError("Username or password is incorrect. ")
    
class signUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username required."),  
        Length(min=4, max=25, message="Username must be between 4 and 25 characters.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password required."), 
        Length(min=8, message="Password must be more than 8 characters long")])
    confirm_password = PasswordField('Password', validators=[DataRequired(message="Password required."), 
        EqualTo('password', message='Password must match.')])
    profile_picture = FileField("Profile Picture")
    submit = SubmitField('Sign Up')

    #username cannot be in existing dataset
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is taken. Please choose another.')
    
    #password must have one special character and one number
    def validate_password(self, password):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        numbers = ['0', '1', '2,', '3', '4', '5', '6', '7', '8', '9']
        if regex.search(password.data) == None:
            raise ValidationError('Password must have one special character and digit.')
        else:
            has_number = any([char in password.data for char in numbers])
            print(has_number)
            if (has_number == False):
                raise ValidationError('Password must have one special character and digit.')
    
class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username required.")])
    password = PasswordField('Password', validators=[DataRequired(message="Password required."), invalid_credentials])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    submit = SubmitField('Post')

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")