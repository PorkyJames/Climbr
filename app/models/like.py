from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


# class Like(db.Model, UserMixin):
#     __tablename__ = 'likes'
#     like_id = db.Column(db.Integer, primary_key=True)
#     post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     # Relationships
#     post = db.relationship('Post', foreign_keys=[post_id], backref=db.backref('post_likes', lazy=True))
#     user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('friendships_initiated', lazy=True))

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'post_id': self.post_id,
#             'user_id': self.user_id
#         }
