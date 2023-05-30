import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from src.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = sa.Column(sa.String(length=100), nullable=False)
    last_name = sa.Column(sa.String(length=100), nullable=False)
    password = sa.Column(sa.String(length=100), nullable=True)
    email = sa.Column(sa.String(length=254), unique=True, nullable=True)
    phone = sa.Column(sa.String(length=15), unique=True, nullable=False)
    todolist_rel = relationship(
        "Todolist",
        back_populates="owner_rel",
    )

