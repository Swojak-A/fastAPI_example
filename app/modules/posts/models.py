from uuid import uuid4

from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False
    )
    title = Column(String(256), index=True, nullable=False)
    content = Column(Text(8192))

    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"<Post={self.id} (title: {self.title[:24] + '...' if len(self.title) > 24 else self.title})>"
