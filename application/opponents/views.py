from application import app, db
from flask import redirect, render_template, request, url_for
from application.opponents.models import Opponent
from application.opponents.forms import OpponentForm
from operator import itemgetter

@app.route("/opponents", methods=["GET"])
def opponents_index():
    return render_template("opponents/list.html", opponents = Opponent.query.all())

@app.route("/opponents/new/")
def opponents_form():
    return render_template("opponents/new.html", form = OpponentForm())
  
@app.route("/opponents/<opponents_id>/", methods=["POST"])
def opponents_change_values(opponents_id):

    t = Opponent.query.get(opponent_id)
    #example:  --> t.done = True
    db.session().commit()
  
    return redirect(url_for("opponents_index"))



@app.route("/opponents/", methods=["POST"])
def opponents_create():

    
    getter = itemgetter("name", "year_of_birth", "strengths", "weaknesses")
    values = getter(request.form)
    t = Opponent(*values)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("opponents_index"))