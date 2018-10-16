from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class CommentForm(FlaskForm):
    name = StringField("Comment name", [validators.Length(min=1, max = 512)])
 
    class Meta:
        csrf = False