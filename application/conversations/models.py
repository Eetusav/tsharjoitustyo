from application import db
from application.models import Base
from sqlalchemy.sql import text

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

    @staticmethod
    def find_comments_for_conversation(convid=0):
      stmt = text("SELECT Comment.id, Comment.name, Comment.conversation_id, Account.username FROM Comment, Account WHERE Account.id = Comment.account_id AND Comment.conversation_id = :convid").params(convid=convid)
      res = db.engine.execute(stmt)
      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "conversation_id":row[2], "username":row[3]})
      return response