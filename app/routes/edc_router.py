from app.config.db_config import get_db
from app.services.edc_service import EDCService
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

edc_router = APIRouter(prefix="/edc", tags=["TEST ROUTER"])
edc_service_obj = EDCService()


@edc_router.get("/metrics-validation")
async def validate_data(req: Request, db: Session = Depends(get_db)):
    return edc_service_obj.validate_data(dict(req.query_params))
