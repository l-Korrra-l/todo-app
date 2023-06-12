from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.user import User
from src.schemas.user_schema import UserCreateSchema
from src.services.db_services.user_db_service import UserDBService
from src.services.token_service import TokenService


class UserService:
    async def create(self, data: UserCreateSchema, session: AsyncSession) -> Dict[str, str]:
        user = await UserDBService.create(
            input_data=UserCreateSchema(**data.dict()),
            session=session,
        )
        return await TokenService.generate_tokens(
            user=user,
        )
