from uuid import UUID

from pydantic import BaseModel


class CommentSchemaBase(BaseModel):
    content: str
    post_id: UUID


class CommentCreateSchema(CommentSchemaBase):
    pass


class CommentSchema(CommentSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
