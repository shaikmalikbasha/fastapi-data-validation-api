from app.routes import metric_group_router, validation_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(validation_router.router)
router.include_router(metric_group_router.metric_group_router)
