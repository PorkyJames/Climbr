from app.models import db, User, environment, SCHEMA
from datetime import datetime

from app.models.comment import Comment
from app.models.post import Post

def seed_comments():
    # Fetch for each User
    demo_user = User.query.filter_by(username="Demo").first()
    marnie_user = User.query.filter_by(username="marnie").first()
    bobbie_user = User.query.filter_by(username="bobbie").first()

    # Create each comment 
    # ! Bobbie comments on Demo's first post
    bobbie_comment = Comment(
        post_id = 1, user_id = 3, text = "This is super helpful! Thanks Demo!", created_at = datetime.utcnow
    )
    # ! Demo responds to Bobbie's comment on their post
    demo_comment = Comment(
        post_id = 2, user_id = 1, text = "No Problem Bobbie! I understand the struggle haha", created_at = datetime.utcnow
    )

    # ! Demo comments on Marnie's post
    demo_comment2 = Comment(
        post_id = 3, user_id = 2, text = "My hands were sweating just watching this!", created_at = datetime.utcnow
    )

    db.session.add(bobbie_comment)
    db.session.add(demo_comment)
    db.session.add(demo_comment2)

    db.session.commit()
