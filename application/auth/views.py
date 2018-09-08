from flask import render_template, request, redirect, url_for
from flask_login import login_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/new", methods=["GET","POST"])
def accounts_create():
    if request.method == "GET":
        return render_template("auth/createform.html", form=LoginForm())

    form = LoginForm(request.form)


    t = User(request.form.get("name"),request.form.get("username"),request.form.get("password"))
   # u = Task(request.form.get("nimimerkki"))

    db.session().add(t)
   # db.session().add(u)
    db.session().commit()
    return redirect(url_for("index"))

