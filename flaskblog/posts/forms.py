from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length




class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired(), Length(min=2, max=40)])
    content = TextAreaField('Content', validators = [DataRequired(), Length(min=2)])
    submit = SubmitField('Post')
