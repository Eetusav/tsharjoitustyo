from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=20)])
    password = PasswordField("Password", [validators.Length(min=5, max=20)])
    name = StringField("Name", [validators.Length(min=3, max=20)])
    password2 = PasswordField("Write password again", [validators.Length(min=5,max=20)])
  
    class Meta:
        csrf = False