 # Add any form classes for Flask-WTF here
 
from flask_wtf import FlaskForm, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired
from wtforms import StringField

class MovieForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    description = TextAreaField('description', validators=[InputRequired()])
    poster = FileField('poster',validators=[FileRequired(),FileAllowed(['jpg',
'png', 'jpeg'], 'Illegal file detected. Ensure your file has a name
and is in one of the following formats: png, jpg, jpeg.')])
