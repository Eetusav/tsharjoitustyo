from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField

class CategoryForm(FlaskForm):
    name = StringField("Category name")
   # done = BooleanField("done")
 
    class Meta:
        csrf = False