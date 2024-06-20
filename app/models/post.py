from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Post(db.Model, UserMixin):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content_text = db.Column(db.String(100), nullable=False)
    media = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'post_id': self.post_id,
            'user_id': self.user_id,
            'content_text': self.content_text,
            'media': self.media,
            'created_at': self.created_at
        }

