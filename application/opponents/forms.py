from flask_wtf import FlaskForm
from wtforms import StringField

class OpponentForm(FlaskForm):
    name = StringField("Opponent's name")
    year_of_birth = StringField("Year of birth")
    strengths = StringField("Strengths in game")
    weaknesses = StringField("Weaknesses in game")
 
    class Meta:
        csrf = False