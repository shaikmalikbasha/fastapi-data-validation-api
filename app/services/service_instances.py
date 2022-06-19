from app.services.metric_group_service import MdMetricGroupService
from app.services.metric_query_service import MdMetricQueryService
from app.services.metric_threshold_service import MdMetricThresholdService
from app.services.metric_instance_service import MdMetricInstanceService

metric_group_service = MdMetricGroupService()
metric_query_service = MdMetricQueryService()
metric_threshold_service = MdMetricThresholdService()
metric_instance_service = MdMetricInstanceService()
