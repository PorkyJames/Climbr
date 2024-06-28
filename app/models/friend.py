from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


# class Friend(db.Model, UserMixin):
#     __tablename__ = 'friends'
#     friendship_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     friend_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow())

#     # Relationships
#     user = db.relationship('User', foreign_keys=[user_id], backref=db.backref('friendships_initiated', lazy=True))
#     friend = db.relationship('User', foreign_keys=[friend_id], backref=db.backref('friendships_received', lazy=True))

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'user_id': self.user.id,
#             'friend_id': self.friend.id,
#             'status': self.status
#         }


