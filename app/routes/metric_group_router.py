from app.config.db_config import get_db
from app.schemas.metric_group_schemas import CreateAndUpdateMetricGroup
from app.services.metric_group_service import MdMetricGroupService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

metric_group_router = APIRouter(prefix="", tags=["MD METRIC GROUP"])

metric_group_service = MdMetricGroupService()


@metric_group_router.get("/groups")
async def get_all_metric_groups(db: Session = Depends(get_db)):
    return metric_group_service.find_all_metric_groups(db)


@metric_group_router.post("/groups")
async def save_metric_group(
    input_body: CreateAndUpdateMetricGroup, db: Session = Depends(get_db)
):
    return metric_group_service.save_metric_group(input_body.dict(), db)


@metric_group_router.get("/groups/{group_name}")
async def get_all_metric_groups(group_name: str, db: Session = Depends(get_db)):
    return metric_group_service.find_metric_group_by_group_name(group_name, db)


@metric_group_router.put("/groups/{group_id}")
async def get_all_metric_groups(
    group_id: int, input_body: CreateAndUpdateMetricGroup, db: Session = Depends(get_db)
):
    return metric_group_service.update_metric_group_by_group_id(
        group_id, input_body.dict(), db
    )


@metric_group_router.delete("/groups/{group_id}")
async def get_all_metric_groups(group_id: int, db: Session = Depends(get_db)):
    return metric_group_service.delete_metric_group_by_group_id(group_id, db)
