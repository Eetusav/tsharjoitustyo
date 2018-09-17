from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class ConversationForm(FlaskForm):
    name = StringField("Conversation name")
   # done = BooleanField("done")
 
    class Meta:
        csrf = False