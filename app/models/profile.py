from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Profile(db.Model, UserMixin):
    __tablename__ = "profiles"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    display_name = db.Column(db.String(30), nullable=False, unique=True)
    bio = db.Column(db.String(50))
    city = db.Column(db.String(50))  
    state = db.Column(db.String(50))   

    # Relationships
    user = db.relationship('User', back_populates='profile')
    
    def to_dict(self):
        return {
            'id': self.id,
            'display_name': self.display_name,
            'bio': self.bio,
            'city': self.city,
            'state': self.state
        }