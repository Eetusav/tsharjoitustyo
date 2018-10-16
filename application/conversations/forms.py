from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ConversationForm(FlaskForm):
    name = StringField("Conversation name", [validators.Length(min=1, max=144, message="Keskustelun tulee olla vähintään 1 merkki ja korkeintaan 144 merkkiä.")])

 
    class Meta:
        csrf = False