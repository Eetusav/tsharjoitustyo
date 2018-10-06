from application import db
from application.models import Base

class Category(Base):

    name = db.Column(db.String(144), nullable=False)
   #conversations = db.relationship("Conversation", backref='conversation', lazy=True)

    def __init__(self, name):
        self.name = name
        #self.done = False