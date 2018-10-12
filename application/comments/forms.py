from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class CommentForm(FlaskForm):
    name = StringField("Comment name", [validators.Length(min=1, max = 144)])
   # done = BooleanField("done")
 
    class Meta:
        csrf = False