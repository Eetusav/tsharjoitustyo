from application import app, db
from flask import redirect, render_template, request, url_for
from application.conversations.models import Conversation
from application.conversations.forms import ConversationForm
from flask_login import login_required, current_user

@app.route("/conversations", methods=["GET"])
def conversations_index():
    return render_template("conversations/list.html", conversations = Conversation.query.all())

@app.route("/conversations/new/")
@login_required
def conversations_form():
    return render_template("conversations/new.html", form = ConversationForm())
  
#@app.route("/comments/<comment_id>/", methods=["POST"])
#@login_required
#def tasks_set_done(task_id):
#
 #   t = Comment.query.get(task_id)
 #   t.done = True
#    db.session().commit()
 # 
#    return redirect(url_for("tasks_index"))

@app.route("/conversations/", methods=["POST"])
@login_required
def conversations_create():
    form = ConversationForm(request.form)
    if not form.validate():
        return render_template("conversations/new.html", form = form)
    t = Conversation(form.name.data)
    #t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("conversations_index"))