from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    # title_text = StringField('Title', validators=[DataRequired(), Length(max=30)])
    content_text = StringField('Content Text', validators=[DataRequired(), Length(min=10, max=255)])
    media = StringField('Embedded Link')
