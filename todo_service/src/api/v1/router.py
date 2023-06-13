from fastapi import APIRouter
from src.api.v1.test import router as test_router
from src.api.v1.user import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(test_router)
router.include_router(user_router)
