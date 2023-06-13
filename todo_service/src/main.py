from fastapi import FastAPI
from fastapi.middleware import Middleware

from src.api.router import router
from src.middlewares.auth_middleware import AuthenticationMiddleware
from starlette_context.middleware import RawContextMiddleware

middlewares = [
    Middleware(RawContextMiddleware),
    Middleware(AuthenticationMiddleware)
]

app = FastAPI(
    docs_url="/api/v1/docs",
    openapi_url="/api/v1/openapi.json",
    redoc_url="/api/v1/redoc",
    middleware=middlewares,
)
api_prefix = "/api"
app.include_router(router, prefix=api_prefix)


@app.get("/")
async def root():
    return {"message": "Hello World"}
