from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ConversationForm(FlaskForm):
    name = StringField("Conversation name", [validators.Length(min=1)])

 
    class Meta:
        csrf = False