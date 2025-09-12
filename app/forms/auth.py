from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class LoginForm(FlaskForm):
    username = StringField(
        'Username or E-Mail',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=64), Regexp(r'^[a-zA-Z0-9_-]+$', message='Usernames may only contain letters, numbers, underscores (_), and dashes (-)')],
    )
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email(), Length(min=6, max=64)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8, max=128)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match.')],
    )
    submit = SubmitField('Register')