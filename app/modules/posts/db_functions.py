from sqlalchemy.orm import Session

from .models import Post
from .schemas import PostCreateSchema


def get_all_posts(db: Session):
    return db.query(Post).all()


def get_single_post(db: Session, post_id: str):
    return db.query(Post).get(post_id)


def create_post(db: Session, post: PostCreateSchema):
    post = Post(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
