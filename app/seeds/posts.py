from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

from ..models.post import Post

def seed_posts():
    demo_user = User.query.filter_by(username='Demo').first()
    marine_user = User.query.filter_by(username='marnie').first()
    # Bobbie will not have any posts
    porky_user = User.query.filter_by(username='Porky').first()

    # Demo User Post #1
    if demo_user:
        first_post_demo = Post(
            user_id=demo_user.id,
            content_text="Look at this new V2 I just flashed! Feeling strong today!",
        )

    # Demo User Post # 2
    if demo_user:
        second_post_demo = Post(
            user_id=demo_user.id,
            content_text="Man this is only a V3?? It felt like a V4+!"
        )

