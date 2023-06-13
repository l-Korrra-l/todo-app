import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.models.base_model import BaseModel


class Todolist(BaseModel):
    __tablename__ = "todolist"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(length=20), nullable=False)
    owner = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner_rel = relationship(
        "User",
        foreign_keys=[owner],
        primaryjoin="Todolist.owner==User.id",
        back_populates="todolist_rel",
    )
    task_rel = relationship(
        "Task",
        back_populates="list_rel",
    )
