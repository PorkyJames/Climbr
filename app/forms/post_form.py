from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title_text = StringField('Title', validators=[DataRequired(), Length(min=10)])
    content_text = StringField('')
    link = StringField('Embedded Link')
