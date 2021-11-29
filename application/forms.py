
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    description = StringField("Add a description : ", validators=[DataRequired()])
    submit = SubmitField("Add")
    date = DateTimeField("Add a Release Date: ")