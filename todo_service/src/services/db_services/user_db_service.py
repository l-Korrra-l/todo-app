from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.mixins.crud_mixin import CRUDMixin
from src.models.user import User
from src.schemas.user_schema import UserCreateSchema, UserUpdateSchema
from passlib.hash import django_pbkdf2_sha256 as handler
from sqlalchemy import or_, select, update


class UserDBService(CRUDMixin):
    table = User
    create_scheme = UserCreateSchema
    update_scheme = UserUpdateSchema

    @classmethod
    async def create(
        cls,
        input_data: create_scheme,
        session: AsyncSession,
        http_exc_text: str = "Record with some unique data exists",
    ):
        input_data.password = handler.hash(input_data.password, rounds=260000, salt_size=22)
        return await super().create(input_data, session)

    @classmethod
    async def get_user_by_email(cls, email: str, session: AsyncSession) -> User:
        query = select(cls.table).filter(cls.table.email == email)
        res = (await session.execute(query)).scalars().first()
        if not res:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return res
