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
  


@app.route("/comments/<comment_id>/update", methods=["POST", "GET"])
@login_required
def comment_update(comment_id):
    if request.method == 'GET':
        return render_template("comments/update.html", form = CommentForm(request.form), comment_id = comment_id, t=Comment.query.get(comment_id))
    form = CommentForm(request.form)
    if not form.validate():
        return render_template("comments/update.html", form = form, comment_id = comment_id, t=Comment.query.get(comment_id))
    d = Comment(form.name.data)
    c = Comment.query.get(comment_id)
    if current_user.id != c.account_id:
        return render_template("comments/list.html", comments = Comment.query.all())
    uusiNimi = d.name
    c.name = uusiNimi
    db.session().commit()
    return redirect(url_for("conversation_view", conversation_id = c.conversation_id))


@app.route("/conversations/<conversation_id>/comment", methods=["POST"])
@login_required
def comments_create(conversation_id):
    form = CommentForm(request.form)
    if not form.validate():
        return redirect(url_for("conversation_view", conversation_id = conversation_id))
    t = Comment(form.name.data)
    t.account_id = current_user.id
    t.conversation_id=conversation_id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("conversation_view", conversation_id = conversation_id))

@app.route("/comments/<comment_id>/delete", methods=["POST"])
@login_required
def comment_delete(comment_id):
    x = Comment.query.get(comment_id)
    conversation_id = x.conversation_id
    if not x.account_id==current_user.id:
        redirect(url_for("conversation_view", conversation_id = conversation_id))
    db.session.delete(x)
    db.session().commit()
    return redirect(url_for("conversation_view", conversation_id = conversation_id))