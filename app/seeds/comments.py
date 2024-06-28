from app.models import db, User, environment, SCHEMA
from datetime import datetime
from sqlalchemy import text

from app.models.comment import Comment
from app.models.post import Post

def seed_comments():
    # Fetch for each User
    demo_user = User.query.filter_by(username="Demo").first()
    marnie_user = User.query.filter_by(username="marnie").first()
    bobbie_user = User.query.filter_by(username="bobbie").first()

    #Fetch for each User's Post
    demo_post = Post.query.filter_by(user_id=demo_user.id, content_text="Hooper's Beta coming in Clutch again! Great information regarding strength vs technique!").first()
    marnie_post = Post.query.filter_by(user_id=marnie_user.id, content_text="Wow. Absolute wow. Alex Honnold tested the limits of humanity and succeeded. I am speechless.").first()

    # Create each comment 
    # ! Bobbie comments on Demo's first post
    bobbie_comment = Comment(
        post_id = demo_post.id, 
        user_id = bobbie_user.id, 
        text = "This is super helpful! Thanks Demo!", 
        created_at = datetime.utcnow()
    )
    # ! Demo responds to Bobbie's comment on their post
    demo_comment = Comment(
        post_id = demo_post.id, 
        user_id = demo_user.id, 
        text = "No Problem Bobbie! Glad I can help!", 
        created_at = datetime.utcnow()
    )

    # ! Demo comments on Marnie's post
    demo_comment2 = Comment(
        post_id = marnie_post.id, 
        user_id = demo_user.id, 
        text = "My hands were sweating just watching this!", 
        created_at = datetime.utcnow()
    )

    db.session.add(bobbie_comment)
    db.session.add(demo_comment)
    db.session.add(demo_comment2)

    db.session.commit()

def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
