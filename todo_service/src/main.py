from fastapi import FastAPI
from src.api import router

app = FastAPI()
api_prefix = "/api"
app.include_router(router, prefix=api_prefix)

@app.get("/")
async def root():
    return {"message": "Hello ffWorld"}


@app.get("/todo/i/")
async def test():
    return {"message": "Hello World"}
