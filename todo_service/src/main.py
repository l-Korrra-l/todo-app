from fastapi import FastAPI
from src.api.router import router

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/openapi.json", redoc_url="/api/v1/redoc")
api_prefix = "/api"
app.include_router(router, prefix=api_prefix)

@app.get("/")
async def root():
    return {"message": "Hello World"}
