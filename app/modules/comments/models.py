from uuid import uuid4

from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False
    )
    content = Column(Text(8192))
    post_id = Column(UUID(as_uuid=True), ForeignKey("posts.id"))

    post = relationship("Post", back_populates="comments")
