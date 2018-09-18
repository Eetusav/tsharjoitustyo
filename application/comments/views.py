from application import app, db
from flask import redirect, render_template, request, url_for
from application.comments.models import Comment
from application.comments.forms import CommentForm
from flask_login import login_required, current_user

@app.route("/comments", methods=["GET"])
def comments_index():
    return render_template("comments/list.html", comments = Comment.query.all())

@app.route("/comments/new/")
@login_required
def comments_form():
    return render_template("comments/new.html", form = CommentForm())
  
#@app.route("/comments/<comment_id>/", methods=["POST"])
#@login_required
#def tasks_set_done(task_id):
#
 #   t = Comment.query.get(task_id)
 #   t.done = True
#    db.session().commit()
 # 
#    return redirect(url_for("tasks_index"))

@app.route("/conversations/<conversation_id>", methods=["POST"])
@login_required
def comments_create(conversation_id):
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("comments/new.html", form = form)
    t = Comment(form.name.data)
    t.account_id = current_user.id
    t.conversation_id=conversation_id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("conversation_view", conversation_id = conversation_id))