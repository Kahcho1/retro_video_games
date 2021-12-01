from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class GamesForm(FlaskForm):
    name = StringField("Title of Game: ", validators=[DataRequired()])
    description = StringField("Summary (Max. 200 words): ")
    date = DateField("Release Date (1990-1999): ", validators=[DataRequired()])
    console = SelectField("Select Platform: ", choices=[])
    submit = SubmitField("Enter")

class ConsoleForm(FlaskForm):
    name = StringField("Add a platform: ", validators=[DataRequired()])
    date = DateField("Release Date (1990-1999): ", validators=[DataRequired()])
    submit = SubmitField("Enter")