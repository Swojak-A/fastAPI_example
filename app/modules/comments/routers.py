from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from modules.core.db import get_db
from .schemas import CommentSchema, CommentCreateSchema
from .db_functions import create_comment

if TYPE_CHECKING:
    from sqlalchemy.orm import Session  # NOQA

router = APIRouter()


@router.post("/", response_model=CommentSchema)
def create_comment_view(post: CommentCreateSchema, db: Session = Depends(get_db)):
    ret = create_comment(db=db, post=post)
    return ret
