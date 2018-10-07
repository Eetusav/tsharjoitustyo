from application import app, db
from flask import redirect, render_template, request, url_for
from application.conversations.models import Conversation
from application.conversations.forms import ConversationForm
from flask_login import login_required, current_user
from application.comments.forms import CommentForm
from application.comments.models import Comment
from application.conversations.models import Subs
from sqlalchemy import desc, asc


@app.route("/conversations/", methods=["GET"])
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
    Conversation.delete_comments_for_conversation(convid=conversation_id)
    db.session.delete(x)
    db.session().commit()
    return redirect(url_for("conversations_index"))

@app.route("/conversations/<conversation_id>/update", methods=["POST"])
@login_required
def conversation_update(conversation_id):
    return redirect(url_for("conversations_index"))

@app.route("/conversations/<conversation_id>/subscribe", methods=["POST"])
@login_required
def conversation_subscribe(conversation_id):
    my_obj = Subs.query.filter(Subs.conversation_id==conversation_id, Subs.account_id==current_user.id).first()
    if my_obj is not None:
        return redirect(url_for("conversations_index"))
    s = Subs(current_user.id, conversation_id)
    s.account_id=current_user.id
    s.conversation_id=conversation_id
    db.session.add(s)
    db.session.commit()
    return redirect(url_for("conversations_index"))

@app.route("/conversations/subscriptions", methods=["GET"])
@login_required
def conversations_subscriptions():
    c = current_user.id
    conversations=Conversation.find_subscriptions(accid=c)
    #subs = Subs.query.all()
    return render_template("conversations/subs.html", conversations=conversations)

@app.route("/conversations/<conversation_id>/subscription/delete", methods=["POST"])
@login_required
def subscription_delete(conversation_id):
    my_obj = Subs.query.filter(Subs.conversation_id==conversation_id, Subs.account_id==current_user.id).first()
    db.session.delete(my_obj)
    db.session().commit()
    return redirect(url_for("conversations_subscriptions"))

#@app.route("/conversations", methods=["GET"])
#@login_required
#def conversations_sort():
#    return render_template("conversations/list.html", conversations=Conversation.query.order_by(asc(Conversation.date_created)).limit(1).all())