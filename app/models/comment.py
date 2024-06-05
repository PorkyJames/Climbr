from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Comment(db.Model, UserMixin):
    __tablename__ = 'comments'

    # Relationships
    
    def to_dict(self):
        return {
            'id': self.id,
        }
