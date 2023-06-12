from sqlalchemy.ext.asyncio import AsyncSession

from src.mixins.crud_mixin import CRUDMixin
from src.models.user import User
from src.schemas.user_schema import UserCreateSchema, UserUpdateScheme
from passlib.hash import django_pbkdf2_sha256 as handler


class UserDBService(CRUDMixin):
    table = User
    create_scheme = UserCreateSchema
    update_scheme = UserUpdateScheme

    @classmethod
    async def create(
        cls,
        input_data: create_scheme,
        session: AsyncSession,
        http_exc_text: str = "Record with some unique data exists",
    ):
        input_data.password = handler.hash(input_data.password, rounds=260000, salt_size=22)
        return await super().create(input_data, session)
