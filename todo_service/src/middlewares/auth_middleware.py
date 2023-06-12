from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from starlette_context import context

from src.core.db import async_session
from src.core.settings import MiddlewareSettings
from src.services.token_service import TokenService

middleware_settings = MiddlewareSettings()


class AuthenticationMiddleware(BaseHTTPMiddleware):
    auth_scheme = HTTPBearer(auto_error=False)

    async def dispatch(self, request, call_next):
        if request.url.path in middleware_settings.ANONYMOUS_ENDPOINTS:
            response = await call_next(request)
            return response

        authorization: HTTPAuthorizationCredentials | None = await self.auth_scheme(request)
        try:
            if not authorization:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={"message": "No authentification token"})

            async with async_session() as session:
                user = await TokenService.decode_jwt(token=authorization.credentials, session=session)
                context["request"] = request
                context["user"] = user

                response = await call_next(request)

                return response

        except HTTPException as exc:
            return JSONResponse(status_code=exc.status_code, content=exc.detail)
