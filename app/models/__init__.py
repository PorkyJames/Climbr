from .db import db
from .db import environment, SCHEMA

from .user import User
from .post import Post
from .comment import Comment
from .like import Like

__all__ = ['User', 'Post', 'Comment', 'Like']

# Establish relationships after all models have been imported
User.posts = db.relationship('Post', backref='author', lazy=True)
User.comments = db.relationship('Comment', backref='commenter', lazy=True)
# User.likes = db.relationship('Like', backref='liker', lazy=True)

Post.comments = db.relationship('Comment', backref='poster', lazy=True)
# Post.likes = db.relationship('Like', backref='post', lazy=True)

Comment.user = db.relationship('User', backref=db.backref('commentUser', lazy=True))
Comment.post = db.relationship('Post', backref=db.backref('commentViewer', lazy=True))