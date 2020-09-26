from typing import TYPE_CHECKING, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.db import get_db
from .schemas import PostCreateSchema, PostSchema
from .db_functions import get_posts, create_post

if TYPE_CHECKING:
    from sqlalchemy.orm import Session  # NOQA

router = APIRouter()


@router.get("/", response_model=List[PostSchema])
def list_all_posts_view(db: Session = Depends(get_db)):
    posts = get_posts(db=db)
    return posts

@router.post("/", response_model=PostSchema)
def create_post_view(post: PostCreateSchema, db: Session = Depends(get_db)):
    ret = create_post(db=db, post=post)
    return ret
