from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
import uuid

from todo_service.src.enums.task_status import TaskStatusEnum


class Todolist:
    __tablename__ = "todolist"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(length=20), nullable=False)
    owner = Column(UUID, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    owner_rel = relationship(
        "User",
        foreign_keys=[owner],
        primaryjoin="Todolist.owner==User.id",
        back_populates="todolist_rel",
    )
