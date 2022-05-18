from typing import Optional
from pydantic import BaseModel


class CreateAndUpdateMetricGroup(BaseModel):
    md_metric_group_name: str


class MdMetricGroupResponse(CreateAndUpdateMetricGroup):
    id: Optional[int]
    is_active: bool

    md_metric_queries: list = []

    class Config:
        orm_mode = True
