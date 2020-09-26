from uuid import UUID

from pydantic import BaseModel


class PostSchemaBase(BaseModel):
    title: str
    content: str

class PostCreateSchema(PostSchemaBase):
    pass

class PostSchema(PostSchemaBase):
    id: UUID

    class Config:
        orm_mode = True
