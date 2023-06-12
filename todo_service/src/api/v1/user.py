from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_session
from src.schemas.token_schema import LoginTokens
from src.schemas.user_schema import UserCreateSchema
from src.services.user_service import UserService

router = APIRouter(prefix="/user")


@router.get("/")
async def user_get():
    return {"message": "Hello user"}


@router.post("/sign-up/", response_model=LoginTokens)
async def sign_up(data: UserCreateSchema, session: AsyncSession = Depends(get_session)):
    return await UserService().create(data=data, session=session)
