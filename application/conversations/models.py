from application import db
from application.models import Base
from sqlalchemy.sql import text

#caco = db.Table('caco', db.Colum('category_id', db.Integer, db.ForeignKey('category.id')), db.Column('conversation_id', db.Integer, db.ForeignKey('conversation.id')))

class Conversation(Base):

    __tablename__ = "conversation"

    name = db.Column(db.String(144), nullable=False)
  #  nimimerkki = db.Column(db.String(144), nullable=False)
   # done = db.Column(db.Boolean, nullable=False)
   # comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'),  nullable=False)
   #comments = db.relationship("Comment", backref='comment', lazy=True)
  # comments = db.relationship("Comment", backref='conversation', lazy=False)
  #conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=True)
  #categories = db.relationship('Category', secondary=caco, backref=db.backref('cacos', lazy=True))

    def __init__(self, name):
        self.name = name
        #self.done = False

    @staticmethod
    def find_comments_for_conversation(convid=0):
      stmt = text("SELECT Comment.id, Comment.name, Comment.conversation_id, Account.username, Comment.account_id FROM Comment, Account WHERE Account.id = Comment.account_id AND Comment.conversation_id = :convid").params(convid=convid)
      res = db.engine.execute(stmt)
      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "conversation_id":row[2], "username":row[3], "account_id":row[4]})
      return response
  
    @staticmethod
    def find_subscriptions(accid=0):
      stmt = text("SELECT Conversation.id, Conversation.name, Subs.conversation_id FROM Conversation LEFT JOIN Subs ON Subs.conversation_id=Conversation.id WHERE Subs.account_id=:accid").params(accid=accid)
      res = db.engine.execute(stmt)
      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "conversation_id":row[2]})
      return response
#class Caco(Base):
#  conversation_id=db.Column(db.Integer, db.ForeignKey('conversation.id'))
#  category_id=db.Column(db.Integer, db.ForeignKey('category.id'))

class Subs(Base):
  conversation_id=db.Column(db.Integer, db.ForeignKey('conversation.id'))
  account_id=db.Column(db.Integer, db.ForeignKey('account.id'))
  def __init__(self, conv_id, acc_id):
        self.conversation_id = conv_id
        self.account_id = acc_id