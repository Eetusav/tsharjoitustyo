from application import app, db
from flask import redirect, render_template, request, url_for
from application.categories.models import Category
from application.categories.forms import CategoryForm
from application.conversations.forms import ConversationForm
from flask_login import login_required, current_user
#from application.comments.forms import CommentForm
#from application.comments.models import Comment


@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories=Category.query.all())


@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form=CategoryForm())

# @app.route("/comments/<comment_id>/", methods=["POST"])
# @login_required
# def tasks_set_done(task_id):
#
 #   t = Comment.query.get(task_id)
 #   t.done = True
#    db.session().commit()
 #
#    return redirect(url_for("tasks_index"))


@app.route("/categories/<category_id>", methods=["GET","POST"])
@login_required
def category_view(category_id):
    form = ConversationForm(request.form)
    return render_template("categories/viewOne.html", t=Category.query.get(category_id), form=form)
#    return render_template("categories/viewOne.html", t=Category.query.get(category_id), form=form, category_comments=Category.find_comments_for_conversation(conversation_id))



@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)
    if not form.validate():
        return render_template("categories/new.html", form=form)
    t = Category(form.name.data)
    #t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
    return redirect(url_for("categories_index"))


#@app.route("/categories/<category_id>/delete", methods=["POST"])
#@login_required
#def conversation_delete(category_id):
#    x = Category.query.get(category_id)
#    db.session.delete(x)
#    db.session().commit()
#    return redirect(url_for("categories_index"))

#@app.route("/categories/<conversation_id>/update", methods=["POST"])
#@login_required
#def conversation_update(conversation_id):
#    return redirect(url_for("categories_index"))