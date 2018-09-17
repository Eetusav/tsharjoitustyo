from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class CommentForm(FlaskForm):
    name = StringField("Comment name")
   # done = BooleanField("done")
 
    class Meta:
        csrf = False