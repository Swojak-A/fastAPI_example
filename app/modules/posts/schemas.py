from typing import List
from uuid import UUID

from pydantic import BaseModel

from modules.comments.schemas import CommentSchema


class PostSchemaBase(BaseModel):
    title: str
    content: str


class PostCreateSchema(PostSchemaBase):
    pass


class PostSchema(PostSchemaBase):
    id: UUID
    comments: List[CommentSchema] = []

    class Config:
        orm_mode = True
