import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from src.enums.task_status import TaskStatusEnum
from src.models.base_model import BaseModel


class Task(BaseModel):
    __tablename__ = "task"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = sa.Column(sa.Enum(TaskStatusEnum), default=TaskStatusEnum.IN_PROGRESS.value, nullable=False)
    content = sa.Column(sa.String(length=100), nullable=False)
    list = sa.Column(UUID, sa.ForeignKey("todolist.id", ondelete="CASCADE"), nullable=False)
    list_rel = relationship(
        "Todolist",
        foreign_keys=[list],
        primaryjoin="Todolist.owner==User.id",
        back_populates="todolist_rel",
    )