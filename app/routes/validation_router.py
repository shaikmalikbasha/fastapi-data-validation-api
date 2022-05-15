from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.db_config import get_db

# from app.schemas import CreateQueryAndThreshold
from app.services.validation_services import ValidationService


router = APIRouter(prefix="", tags=["Validation API"])

validation_service = ValidationService()


# @router.get("/instance")
# def fetch_all_md_instances(db: Session = Depends(get_db)):
#     return validation_service.get_all_md_instance(db)


# @router.post("/queries")
# def add_queries(input_body: CreateQueryAndThreshold, db: Session = Depends(get_db)):
#     print(input_body)
#     # return validation_service.add_queries_for_groups(db, input_body.dict())
#     return input_body.dict()


# @router.get("/add-metadata-columns")
# async def add_metadata_columns():
#     return {"success": True, "msg": "Metadata columns were addedd successfully"}


# @router.get("/validate-data")
# async def validate_data():
#     return {"msg": "Validation started"}
