from app.routes import (
    metric_group_router,
    metric_query_router,
    metric_threshold_router,
    test_router,
    edc_router,
)
from fastapi import APIRouter

router = APIRouter()

# Register routes for your endpoints here.
router.include_router(metric_group_router.metric_group_router)
router.include_router(metric_query_router.metric_query_router)
router.include_router(metric_threshold_router.metric_threshold_router)
router.include_router(edc_router.edc_router)
router.include_router(test_router.test_router)
