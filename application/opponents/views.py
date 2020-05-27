from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/opponents", methods=["GET"])
def opponents_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/opponents/new/")
def opponents_form():
    return render_template("tasks/new.html", form = TaskForm())
  
#@app.route("/opponents/<opponents_id>/", methods=["POST"])
#def opponents_set_done(opponents_id):

#    t = Task.query.get(task_id)
#    t.done = True
#    db.session().commit()
  
#    return redirect(url_for("opponents_index"))

@app.route("/opponents/", methods=["POST"])
def opponents_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("opponents_index"))