import datetime

import jwt
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.settings import SettingsJWT
from src.models.user import User
from src.services.db_services.user_db_service import UserDBService

jwt_settings = SettingsJWT()


class TokenService:
    async def encode_access_token(user: User) -> str:
        payload = {
            "user_id": str(user.id),
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=jwt_settings.JWT_EXP_MIN),
        }
        token = jwt.encode(payload, jwt_settings.JWT_SECRET_KEY, algorithm=jwt_settings.JWT_ALGORITHM)
        print(token)
        print(jwt_settings.JWT_REFRESH_SECRET_KEY)
        print(jwt_settings.JWT_ALGORITHM)
        return token

    async def encode_refresh_token(user: User) -> str:
        payload = {
            "user_id": str(user.id),
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=jwt_settings.JWT_REFRESH_EXP_MIN),
        }
        token = jwt.encode(payload, jwt_settings.JWT_REFRESH_SECRET_KEY, algorithm=jwt_settings.JWT_ALGORITHM)
        return token

    @staticmethod
    async def generate_tokens(user: User):
        access_token = await TokenService.encode_access_token(user)
        refresh_token = await TokenService.encode_refresh_token(user)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    @staticmethod
    async def decode_jwt(token: str, session: AsyncSession, secret_key: str = None) -> User:
        try:
            if secret_key:
                payload = jwt.decode(token, secret_key, algorithms=[jwt_settings.JWT_ALGORITHM])
            else:
                payload = jwt.decode(token, jwt_settings.JWT_SECRET_KEY, algorithms=[jwt_settings.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Token Expired"})
        except BaseException:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "Authorization Failed"}
            )

        user = await UserDBService.retrieve(pk=payload["user_id"], session=session)
        return user

    @staticmethod
    async def decode_refresh_jwt(token: str, session: AsyncSession) -> User:
        try:
            payload = jwt.decode(
                token,
                jwt_settings.JWT_REFRESH_SECRET_KEY,
                algorithms=[jwt_settings.JWT_ALGORITHM],
            )
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Refresh token expired")
        except BaseException:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization failed.")
        return await UserDBService.retrieve(payload["user_id"], session)
