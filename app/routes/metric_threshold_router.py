from typing import List

from app.config.db_config import get_db
from app.schemas.metric_threshold_schemas import (
    CreateAndUpdateMetricThreshold,
    MetricThresholdResponse,
)
from app.services.metric_threshold_service import MdMetricThresholdService
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

metric_threshold_router = APIRouter(prefix="/thresholds", tags=["MD_METRIC_THRESHOLDS"])
metric_threshold_service = MdMetricThresholdService()


@metric_threshold_router.get(
    "/",
    response_model=List[MetricThresholdResponse],
    status_code=200,
)
async def get_all_metric_thresholds(db: Session = Depends(get_db)):
    return metric_threshold_service.find_all_metric_thresholds(db)


@metric_threshold_router.post("/", status_code=201)
async def add_metric_thresholds(
    input_body: CreateAndUpdateMetricThreshold, db: Session = Depends(get_db)
):
    return metric_threshold_service.save_metric_threshold(input_body.dict(), db)


@metric_threshold_router.get(
    "/{threshold_id}",
    response_model=MetricThresholdResponse,
    status_code=status.HTTP_200_OK,
)
async def get_all_metric_threshold_by_id(
    threshold_id: int, db: Session = Depends(get_db)
):
    return metric_threshold_service.find_metric_threshold_by_id(threshold_id, db)


@metric_threshold_router.put("/{threshold_id}", status_code=status.HTTP_202_ACCEPTED)
async def modify_metric_threshold_by_id(
    threshold_id: int,
    input_body: CreateAndUpdateMetricThreshold,
    db: Session = Depends(get_db),
):
    return metric_threshold_service.update_metric_threshold_by_id(
        threshold_id, input_body, db
    )


@metric_threshold_router.delete("/{threshold_id}", status_code=status.HTTP_202_ACCEPTED)
async def remove_metric_threshold_by_id(
    threshold_id: int, db: Session = Depends(get_db)
):
    return metric_threshold_service.delete_metric_threshold_by_id(threshold_id, db)
