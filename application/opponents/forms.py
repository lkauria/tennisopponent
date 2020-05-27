from flask_wtf import FlaskForm
from wtforms import StringField

class OpponentForm(FlaskForm):
    name = StringField("Opponent's name")
    year_of_birth = StringField("Year of birth")
 
    class Meta:
        csrf = False