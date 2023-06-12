import datetime

import jwt

from src.core.settings import SettingsJWT
from src.models.user import User

jwt_settings = SettingsJWT()


class TokenService:
    async def encode_access_token(user: User) -> str:
        payload = {
            "user_id": str(user.id),
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=jwt_settings.JWT_EXP_MIN),
        }
        token = jwt.encode(payload, jwt_settings.JWT_SECRET_KEY, algorithm=jwt_settings.JWT_ALGORITHM)

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
