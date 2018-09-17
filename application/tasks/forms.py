from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class TaskForm(FlaskForm):
    name = StringField("Task name")
    done = BooleanField("done")
 
    class Meta:
        csrf = False