from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo


class UpdateUsernameForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=3, max=64), Regexp(r'^[a-zA-Z0-9_-]+$', message='Usernames may only contain letters, numbers, underscores (_), and dashes (-)')]
    )
    current_password = PasswordField(
        'Current Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Update Username')

class UpdateEmailForm(FlaskForm):
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email(), Length(min=6, max=64)]
    )
    current_password = PasswordField(
        'Current Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Update Email')

class UpdatePasswordForm(FlaskForm):
    current_password = PasswordField(
        'Current Password',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'New Password',
        validators=[DataRequired(), Length(min=8, max=128)]
    )
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[DataRequired(), EqualTo('password', message='Passwords must match.')],
    )
    submit = SubmitField('Update Password')

class UpdateBiographyForm(FlaskForm):
    biography = TextAreaField(
        'Biography',
        validators=[Length(max=250)],
    )
    submit = SubmitField('Update Biography')

class UpdateAvatarForm(FlaskForm):
    avatar = FileField(
        'Avatar',
        validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'])],
    )
    submit = SubmitField('Update Avatar')