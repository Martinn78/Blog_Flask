from myblog import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullabel=False)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    def __init__(self, author, title, body):
        self.author = author
        self.title = self.title
        self.body = self.body
        
    def __repr__(self, title):
        return f'Post: {title}'