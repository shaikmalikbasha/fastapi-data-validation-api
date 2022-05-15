from pydantic import BaseModel


class CreateQueryAndThreshold(BaseModel):
    md_metric_group_name: str
    md_metric_query_name: str
    md_metric_sql_query: str
    md_meytric_threshold_value: str
