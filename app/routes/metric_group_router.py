from typing import List

from app.config.db_config import get_db
from app.schemas.metric_group_schemas import (
    CreateAndUpdateMetricGroup,
    MdMetricGroupResponse,
)
from app.services.service_instances import metric_group_service
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

metric_group_router = APIRouter(prefix="/groups", tags=["MD_METRIC_GROUP"])


@metric_group_router.get(
    "/", response_model=List[MdMetricGroupResponse], status_code=200
)
async def get_all_metric_groups(db: Session = Depends(get_db)):
    return metric_group_service.find_all_metric_groups(db)


@metric_group_router.post("/", status_code=201)
async def save_metric_group(
    input_body: CreateAndUpdateMetricGroup, db: Session = Depends(get_db)
):
    return metric_group_service.save_metric_group(input_body.dict(), db)


@metric_group_router.get("/{group_name}")
async def get_metric_group_by_group_name(
    group_name: str, db: Session = Depends(get_db)
):
    return metric_group_service.find_metric_group_by_group_name(group_name, db)


@metric_group_router.put("/{group_id}")
async def update_metric_group_by_id(
    group_id: int, input_body: CreateAndUpdateMetricGroup, db: Session = Depends(get_db)
):
    return metric_group_service.update_metric_group_by_group_id(
        group_id, input_body.dict(), db
    )


@metric_group_router.delete("/{group_id}")
async def remove_metric_group_by_id(group_id: int, db: Session = Depends(get_db)):
    return metric_group_service.delete_metric_group_by_group_id(group_id, db)
