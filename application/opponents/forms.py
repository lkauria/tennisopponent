from flask_wtf import FlaskForm
from wtforms import StringField

class OpponentForm(FlaskForm):
    name = StringField("Opponent's name")
 
    class Meta:
        csrf = False