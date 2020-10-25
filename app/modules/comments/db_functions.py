from sqlalchemy.orm import Session

from .models import Comment
from .schemas import CommentCreateSchema


def create_comment(db: Session, post: CommentCreateSchema):
    post = Comment(**post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
