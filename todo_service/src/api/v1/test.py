from fastapi import APIRouter

router = APIRouter(prefix="/test")

@router.get("/")
async def test_get():
    return {"message": "Hello ffWorldsdd"}

