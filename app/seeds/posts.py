from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

from ..models.post import Post

def seed_posts():
    demo_user = User.query.filter_by(username='Demo').first()
    marnie_user = User.query.filter_by(username='marnie').first()

    #Bobbie and Porky will not have any posts for testing purposes.

    # Check if the user exists and then create posts
    if demo_user:
        demo_post1 = Post(
            user_id=demo_user.id,
            content_text="Hooper's Beta coming in Clutch again! Great information regarding strength vs technique!",
            media="https://www.youtube.com/embed/EHBDWVs36Ko?si=bb8LpH44_OPSd0Q8",
            created_at=datetime.utcnow()
        )
        db.session.add(demo_post1)

    if demo_user: 
        demo_post2 = Post(
            user_id=demo_user.id,
            content_text="LMAO what?? How does he climb the side like that?",
            media="https://youtube.com/embed/PTVRoDBhdY8?si=Bl4Cx6UOPt8g5ESU",
            created_at=datetime.utcnow()
        )
        db.session.add(demo_post2)

    if marnie_user:
        marnie_post1 = Post(
            user_id=marnie_user.id,
            content_text="Wow. Absolute wow. Alex Honnold tested the limits of humanity and succeeded. I am speechless.",
            media="https://www.youtube.com/embed/V4OGs1DehzA?si=GYQq-4suZAiGjlVU",
            created_at=datetime.utcnow()
        )
        db.session.add(marnie_post1)

    # Commit the changes to the database
    db.session.commit()

