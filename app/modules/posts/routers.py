from typing import TYPE_CHECKING, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from modules.core.db import get_db
from .schemas import PostCreateSchema, PostSchema
from .db_functions import get_all_posts, get_single_post, create_post

if TYPE_CHECKING:
    from sqlalchemy.orm import Session  # NOQA

router = APIRouter()


@router.get("/", response_model=List[PostSchema])
def list_all_posts_view(db: Session = Depends(get_db)):
    posts = get_all_posts(db=db)
    return posts


@router.get("/{post_id}", response_model=PostSchema)
def retrieve_post_view(post_id: str, db: Session = Depends(get_db)):
    post = get_single_post(db=db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostSchema)
def create_post_view(post: PostCreateSchema, db: Session = Depends(get_db)):
    ret = create_post(db=db, post=post)
    return ret
