from application import db
from application.models import Base

class Category(Base):

    name = db.Column(db.String(144), nullable=False)
  #  nimimerkki = db.Column(db.String(144), nullable=False)
   # done = db.Column(db.Boolean, nullable=False)
   # comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'),  nullable=False)
   #comments = db.relationship("Comment", backref='comment', lazy=True)

    def __init__(self, name):
        self.name = name
        #self.done = False