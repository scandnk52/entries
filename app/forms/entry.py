from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EntryForm(FlaskForm):
    content = TextAreaField(
        'Content',
        validators=[DataRequired(), Length(min=2, max=1000)],
    )
    submit = SubmitField('Create Entry')