from app.config.db_config import get_db
from app.services.service_instances import metric_instance_service
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

edc_router = APIRouter(prefix="/edc", tags=["TEST ROUTER"])


@edc_router.get("/metrics-validation")
async def validate_data(req: Request, db: Session = Depends(get_db)):
    return metric_instance_service.save_metric_instance(dict(req.query_params), db)
