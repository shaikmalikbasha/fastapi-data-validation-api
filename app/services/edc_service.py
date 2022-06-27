from app.services.metric_instance_service import MdMetricInstanceService

metric_instance_service = MdMetricInstanceService()


class EDCService:
    def validate_data(self, input_body: dict):
        # Check whether group name has given or not
        # Add an entry in the Instance Table
        #
        input_body = metric_instance_service.metric_instance_param_parser(input_body)
        print(f"After: {input_body}")
        return input_body
