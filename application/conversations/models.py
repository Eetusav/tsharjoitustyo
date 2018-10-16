from application import db
from application.models import Base
from sqlalchemy.sql import text


class Conversation(Base):

    __tablename__ = "conversation"

    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),  nullable=False)
  

    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_comments_for_conversation(convid=0):
      stmt = text("SELECT Comment.id, Comment.name, Comment.conversation_id, Account.username, Comment.account_id, Comment.date_created,  (select COUNT(Comment.id) FROM Comment WHERE Comment.conversation_id=:convid) FROM Comment, Account WHERE Account.id = Comment.account_id AND Comment.conversation_id = :convid").params(convid=convid)
      res = db.engine.execute(stmt)
      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "conversation_id":row[2], "username":row[3], "account_id":row[4], "date":row[5], "count":row[6]})
      return response
  
    @staticmethod
    def find_subscriptions(accid=0):
      stmt = text("SELECT Conversation.id, Conversation.name, Subs.conversation_id, (select COUNT(Subs.conversation_id) FROM Subs WHERE Subs.account_id=:accid) FROM Conversation LEFT JOIN Subs ON Subs.conversation_id=Conversation.id WHERE Subs.account_id=:accid").params(accid=accid)
      res = db.engine.execute(stmt)
      response = []
      for row in res:
        response.append({"id":row[0], "name":row[1], "conversation_id":row[2], "count":row[3]})
      return response
    
    @staticmethod
    def delete_comments_for_conversation(convid=0):
      stmt = text("DELETE FROM Comment WHERE Comment.conversation_id = :convid").params(convid=convid)
      res = db.engine.execute(stmt)


class Subs(Base):
  conversation_id=db.Column(db.Integer, db.ForeignKey('conversation.id'))
  account_id=db.Column(db.Integer, db.ForeignKey('account.id'))
  def __init__(self, conv_id, acc_id):
        self.conversation_id = conv_id
        self.account_id = acc_id