from typing import TypeVar

from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import Base

TableType = TypeVar("TableType", bound=Base)
CreateBaseSchema = TypeVar("CreateBaseSchema", bound=BaseModel)
UpdateBaseSchema = TypeVar("UpdateBaseSchema", bound=BaseModel)


class CRUDMixin:
    table: TableType = None
    create_scheme: CreateBaseSchema = None
    update_scheme: UpdateBaseSchema = None

    @classmethod
    async def create(
        cls,
        input_data: create_scheme,
        session: AsyncSession,
        http_exc_text: str = "Record with some unique data exists",
    ):
        """Create model using Pydantic schema."""
        try:
            obj = cls.table(**input_data.dict())
            session.add(obj)
            await session.commit()
        except IntegrityError:
            raise HTTPException(detail=http_exc_text, status_code=status.HTTP_400_BAD_REQUEST)
        await session.refresh(obj)
        return obj
