from application import app, db
from flask import redirect, render_template, request, url_for
from application.opponents.models import Opponent
from application.opponents.forms import OpponentForm

@app.route("/opponents", methods=["GET"])
def opponents_index():
    return render_template("opponents/list.html", opponents = Opponent.query.all())

@app.route("/opponents/new/")
def opponents_form():
    return render_template("opponents/new.html", form = OpponentForm())
  
@app.route("/opponents/<opponents_id>/", methods=["POST"])
def opponents_set_done(opponents_id):

    t = Opponent.query.get(opponent_id)
    db.session().commit()
  
    return redirect(url_for("opponents_index"))

@app.route("/opponents/", methods=["POST"])
def opponents_create():
    t = Opponent(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("opponents_index"))