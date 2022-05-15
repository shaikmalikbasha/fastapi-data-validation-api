from typing import Optional
from pydantic import BaseModel


class CreateAndUpdateMetricGroup(BaseModel):
    md_metric_group_name: str


class MdMetricGroupResponse(BaseModel):
    id: Optional[str]
    md_metric_group_name: str
    is_active: bool

    class Config:
        orm_mode = True
