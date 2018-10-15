from application import db
from application.models import Base

class Comment(Base):

    name = db.Column(db.String(144), nullable=False)
  #  nimimerkki = db.Column(db.String(144), nullable=False)
   # done = db.Column(db.Boolean, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),  nullable=False, lazy=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=True, lazy=True)
    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)

    def __init__(self, name):
        self.name = name
        #self.done = False