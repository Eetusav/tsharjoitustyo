from application import db
from application.models import Base

class Conversation(Base):

    __tablename__ = "conversation"

    name = db.Column(db.String(144), nullable=False)
  #  nimimerkki = db.Column(db.String(144), nullable=False)
   # done = db.Column(db.Boolean, nullable=False)
   # comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'),  nullable=False)
   #comments = db.relationship("Comment", backref='comment', lazy=True)
  # comments = db.relationship("Comment", backref='conversation', lazy=False)

    def __init__(self, name):
        self.name = name
        #self.done = False