import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from todo_service.src.enums.task_status import TaskStatusEnum


class Task:
    __tablename__ = "task"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = sa.Column(sa.Enum(*TaskStatusEnum.values()), default=TaskStatusEnum.IN_PROGRESS.value, nullable=False)
    content = sa.Column(sa.String(length=100), nullable=False)