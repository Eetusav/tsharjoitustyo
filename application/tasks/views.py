from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from flask_login import login_required

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/tasks/new/")
@login_required
def tasks_form():
    return render_template("tasks/new.html")
  
@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    t = Task(request.form.get("name"),request.form.get("nimimerkki"))
   # u = Task(request.form.get("nimimerkki"))

    db.session().add(t)
   # db.session().add(u)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))