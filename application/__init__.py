# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)
import os

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comments.db"    
    app.config["SQLALCHEMY_ECHO"] = True


# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

#ff
# oman sovelluksen toiminnallisuudet
from application import views
from application.comments import models
from application.comments import views
from application.auth import models
from application.auth import views
from application.auth import forms

# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()