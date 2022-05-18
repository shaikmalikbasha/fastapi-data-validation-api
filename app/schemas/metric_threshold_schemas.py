from typing import Optional

from app.config.vars_config import settings
from app.utils.constants import ACTIVE_STATUS
from pydantic import BaseModel


class CreateAndUpdateMetricThreshold(BaseModel):
    md_metric_threshold_type: str
    md_metric_threshold_value: str
    md_metric_threshold_failure_text: Optional[str]
    md_metric_threshold_action: Optional[str] = "NOTIFICATION"
    md_metric_threshold_action_parameters: Optional[str] = settings.ADMIN_MAIL
    md_metric_threshold_status: Optional[str] = ACTIVE_STATUS
    md_metric_query_id: int


class MetricThresholdResponse(CreateAndUpdateMetricThreshold):
    id: Optional[int]

    class Config:
        orm_mode = True
