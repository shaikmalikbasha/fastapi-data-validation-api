from typing import Optional

from app.utils.constants import SUCCESS_STATUS
from pydantic import BaseModel


class CreateAndUpdateMetricQuery(BaseModel):
    md_metric_query_name: str
    md_metric_sql_query: str
    md_metric_query_status: Optional[str] = SUCCESS_STATUS
