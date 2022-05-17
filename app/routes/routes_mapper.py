from app.routes import metric_group_router, metric_query_router, metric_threshold_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(metric_group_router.metric_group_router)
router.include_router(metric_query_router.metric_query_router)
router.include_router(metric_threshold_router.metric_threshold_router)
