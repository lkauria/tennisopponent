from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, IntegerField
from wtforms.validators import NumberRange

class OpponentForm(FlaskForm):
    name = StringField("Opponent's name", [validators.Length(min=2)])
    year_of_birth = IntegerField("Year of birth", [validators.NumberRange(min=1900, max=2100, message=None)])
    strengths = StringField("Strengths in game")
    weaknesses = StringField("Weaknesses in game")
 
    class Meta:
        csrf = False