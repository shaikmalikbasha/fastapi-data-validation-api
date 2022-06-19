from typing import Optional

from pydantic import BaseModel


class CreateMetricInstance(BaseModel):
    md_metric_schedule_id: Optional[int] = None
    md_metric_group_name: str


class UpdateMetricInstance(BaseModel):
    md_metric_instance_id: int
    md_metric_schedule_id: Optional[int] = None
    md_metric_group_name: Optional[str] = None
    md_metric_instance_custom_paramaters: Optional[str] = None
    md_metric_instance_status: Optional[str] = None
    md_metric_instance_failure_text: Optional[str] = None
    md_metric_instance_query_attempt_count: Optional[int] = None
    md_metric_instance_query_complete_count: Optional[int] = None
    md_metric_instance_query_attempt_count: Optional[int] = None
