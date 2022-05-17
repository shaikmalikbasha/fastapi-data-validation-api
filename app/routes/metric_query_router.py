from app.config.db_config import get_db
from app.schemas.metric_query_schema import CreateAndUpdateMetricQuery
from app.services.metric_query_service import MdMetricQueryService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

metric_query_router = APIRouter(prefix="/queries", tags=["MD_METRIC_QUERY"])


metric_query_service = MdMetricQueryService()


@metric_query_router.get("/", status_code=200)
async def get_all_metric_queries(db: Session = Depends(get_db)):
    return metric_query_service.find_all_metric_queries(db)


@metric_query_router.post("/", status_code=201)
async def save_metric_group(
    input_body: CreateAndUpdateMetricQuery, db: Session = Depends(get_db)
):
    return metric_query_service.save_metric_query(input_body.dict(), db)


@metric_query_router.get("/{metric_id}")
async def get_metric_query(metric_id: int, db: Session = Depends(get_db)):
    return metric_query_service.find_metric_query_by_id(metric_id, db)


@metric_query_router.put("/{metric_id}")
async def modify_metric_query_by_id(
    metric_id: int,
    input_body: CreateAndUpdateMetricQuery,
    db: Session = Depends(get_db),
):
    return metric_query_service.update_metric_query_by_id(
        metric_id, input_body.dict(), db
    )


@metric_query_router.delete("/{metric_id}")
async def remove_metric_query_by_id(metric_id: int, db: Session = Depends(get_db)):
    return metric_query_service.delete_metric_query(metric_id, db)
