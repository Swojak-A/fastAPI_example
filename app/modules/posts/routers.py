from typing import TYPE_CHECKING, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.db import get_db
from .schemas import PostCreateSchema, PostSchema
from .db_functions import get_posts_func, create_post_func

if TYPE_CHECKING:
    from sqlalchemy.orm import Session  # NOQA

router = APIRouter()


@router.get("/", response_model=List[PostSchema])
def list_all_posts(db: Session = Depends(get_db)):
    posts = get_posts_func(db=db)
    return posts

@router.post("/", response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    ret = create_post_func(db=db, post=post)
    return ret
