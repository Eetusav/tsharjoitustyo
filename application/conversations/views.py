from application import app, db
from flask import redirect, render_template, request, url_for
from application.conversations.models import Conversation
from application.conversations.forms import ConversationForm
from flask_login import login_required, current_user
from application.comments.forms import CommentForm
from application.comments.models import Comment


@app.route("/conversations", methods=["GET"])
def conversations_index():
    return render_template("conversations/list.html", conversations=Conversation.query.all())


@app.route("/conversations/new/")
@login_required
def conversations_form():
    return render_template("conversations/new.html", form=ConversationForm())

# @app.route("/comments/<comment_id>/", methods=["POST"])
# @login_required
# def tasks_set_done(task_id):
#
 #   t = Comment.query.get(task_id)
 #   t.done = True
#    db.session().commit()
 #
#    return redirect(url_for("tasks_index"))


@app.route("/conversations/<conversation_id>", methods=["GET","POST"])
@login_required
def conversation_view(conversation_id):
    form = CommentForm(request.form)
   # if not form.validate():
   #     return render_template("conversations/viewOne.html", form = form)
   # t = Comment(form.name.data)
   # t.account_id = current_user.id
    #t.conversation_id = conversation_id
    # db.session().add(t)
    # db.session().commit()
    return render_template("conversations/viewOne.html", t=Conversation.query.get(conversation_id), form=form, conversation_comments=Conversation.find_comments_for_conversation(conversation_id))



@app.route("/conversations/", methods=["POST"])
@login_required
def conversations_create():
    form = ConversationForm(request.form)
    if not form.validate():
        return render_template("conversations/new.html", form=form)
    t = Conversation(form.name.data)
    #t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("conversations_index"))


@app.route("/conversations/<conversation_id>/delete", methods=["POST"])
@login_required
def conversation_delete(conversation_id):
    x = Conversation.query.get(conversation_id)
    db.session.delete(x)
    db.session().commit()
    return redirect(url_for("conversations_index"))

@app.route("/conversations/<conversation_id>/update", methods=["POST"])
@login_required
def conversation_update(conversation_id):
    return redirect(url_for("conversations_index"))