from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length

from app.forms.entry import EntryForm

class TopicForm(EntryForm):
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=2, max=128), Regexp(r"^[\w\s\-_\.,']+$")]
    )
    submit = SubmitField('Create Topic')