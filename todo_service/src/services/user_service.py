from typing import Dict

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.schemas.user_schema import UserCreateSchema, UserLoginSchema
from src.services.db_services.user_db_service import UserDBService
from src.services.token_service import TokenService
from passlib.hash import django_pbkdf2_sha256 as handler


class UserService:
    async def create(self, data: UserCreateSchema, session: AsyncSession) -> Dict[str, str]:
        user = await UserDBService.create(
            input_data=UserCreateSchema(**data.dict()),
            session=session,
        )
        return await TokenService.generate_tokens(
            user=user,
        )

    async def login(self, data: UserLoginSchema, session: AsyncSession) -> Dict[str, str]:
        try:
            user = await UserDBService.get_user_by_email(data.email, session)
        except HTTPException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User with such email does not exist."
            )

        if not handler.verify(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

        return await TokenService.generate_tokens(
            user=user,
        )
