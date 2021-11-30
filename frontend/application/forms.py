from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class GamesForm(FlaskForm):
    name = StringField("Add a name of a game: ", validators=[DataRequired()])
    description = StringField("Add a summary for the game: ")
    date = DateTimeField("Add the game's date of release: ", validators=[DataRequired()])
    submit = SubmitField("Enter")

class ConsoleForm(FlaskForm):
    name = StringField("Add a platform: ", validators=[DataRequired()])
    date = DateTimeField("Add the console's date of release: ", validators=[DataRequired()])
    submit = SubmitField("Enter")