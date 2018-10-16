from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=20, message="Käyttäjätunnuksen tulee olla vähintään 3 ja korkeintaan 20 merkkiä.")])
    password = PasswordField("Password", [validators.Length(min=5, max=20, message="Salasanan tulee olla vähintään 3 ja korkeintaan 20 merkkiä.")])
    name = StringField("Name", [validators.Length(min=3, max=20, message="Nimen tulee olla vähintään 5 ja korkeintaan 20 merkkiä.")])
    password2 = PasswordField("Write password again", [validators.Length(min=5,max=20, message="Salasanan tulee olla vähintään 5 ja korkeintaan 20 merkkiä.")])
  
    class Meta:
        csrf = False