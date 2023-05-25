from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/test")

@router.get("/")
async def test_get():
    return {"message": "Hello ffWorldsdd"}

@router.get("/")
async def test_get1():
    return {"message": "Hello ffWorldsdd"}
