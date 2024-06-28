from app.models import db, User, environment, SCHEMA
from datetime import datetime
from sqlalchemy import text

from ..models.post import Post

def seed_posts():
    demo_user = User.query.filter_by(username='Demo').first()
    marnie_user = User.query.filter_by(username='marnie').first()

    #Bobbie will not have any posts for testing purposes.

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
            content_text="Man... tried this V2+ called Bloody Oasis and my fingers are all cut up. Here's what the route looks like! ",
            media="https://mountainproject.com/assets/photos/climb/124289251_medium_1685290583_topo.jpg?cache=1685367500",
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

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
