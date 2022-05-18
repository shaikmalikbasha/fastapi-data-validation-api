from typing import Any, Optional

from app.utils.constants import SUCCESS_STATUS
from pydantic import BaseModel


class CreateAndUpdateMetricQuery(BaseModel):
    md_metric_query_name: str
    md_metric_sql_query: str
    md_metric_query_status: Optional[str] = SUCCESS_STATUS
    md_metric_group_id: int


class MetricQueryResponse(CreateAndUpdateMetricQuery):
    id: Optional[int]
    md_metric_threshold: Any

    class Config:
        orm_mode = True
