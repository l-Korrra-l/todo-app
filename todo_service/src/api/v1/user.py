from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_session
from src.schemas.token_schema import LoginTokens, TokenSchema
from src.schemas.user_schema import UserCreateSchema, UserLoginSchema, GetUserSchema
from src.services.user_service import UserService
from starlette_context import context

router = APIRouter(prefix="/user")


@router.get("/")
async def user_get():
    return {"message": "Hello user"}


@router.post("/sign-up/", response_model=LoginTokens)
async def sign_up(data: UserCreateSchema, session: AsyncSession = Depends(get_session)):
    return await UserService().create(data=data, session=session)


@router.post("/sign-in/", response_model=LoginTokens)
async def login(data: UserLoginSchema, session: AsyncSession = Depends(get_session)):
    return await UserService().login(data=data, session=session)


@router.post("/refresh/", response_model=LoginTokens)
async def refresh(refresh_form: TokenSchema, session: AsyncSession = Depends(get_session)):
    return await UserService.refresh_tokens(refresh_token=refresh_form.token, session=session)


@router.get("/me", response_model=GetUserSchema)
async def get_current_user():
    return context["user"]
