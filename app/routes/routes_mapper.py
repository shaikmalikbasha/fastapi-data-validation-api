from app.routes import validation_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(validation_router.router)
