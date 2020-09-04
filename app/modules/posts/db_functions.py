from sqlalchemy.orm import Session

from .models import Post
from .schemas import PostSchema


def get_posts_func(db: Session):
    return db.query(Post).all()


def create_post_func(db: Session, post: PostSchema):
    post = Post(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post