from app.models.models import MdMetricInstance
from fastapi import HTTPException, status


class MdMetricInstanceService:
    """
    MdMetricInstanceService is the service for MdMetricInstance Table/Entity
    """

    def save_metric_instance(self, req_params, db):
        print(f"REQ-PARAMS: {req_params}")

        if "<GROUP_NAME>" not in req_params:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"msg": "Param <GROUP_NAME> is Missing..."},
            )

        md_metric_instance_custom_paramaters = self.metric_instance_param_parser(
            req_params
        )
        # Create Instance
        new_instance = MdMetricInstance(
            md_metric_group_name=req_params["<GROUP_NAME>"],
            md_metric_instance_custom_paramaters=md_metric_instance_custom_paramaters,
        )

        # Save the instance to database
        db.add(new_instance)
        db.commit()
        db.refresh(new_instance)

        return new_instance

    def find_all_metric_instances(self, db):
        stmt = db.query(MdMetricInstance)
        print(f"SQL QUERY: {stmt}")
        instances = stmt.all()
        print(f"MdMetricGroupResultSet: {instances}")
        return instances

    def find_metric_instance_by_id(self, instance_id, db):
        query = db.query(MdMetricInstance)
        print(f"SQL QUERY: {query}")
        instance = query.first()
        print(f"MdMetricInstanceResult: {instance}")
        if not instance:
            desc = {
                "msg": "Invalid Input",
                "description": f"Instance with id: {instance_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        return instance

    def update_metric_instance_by_id(self, instance_id, input_body, db):
        instance = self.find_metric_instance_by_id(instance_id, db)

        for key, value in input_body.items():
            if value is not None:
                setattr(instance, key, value)

        db.add(instance)
        db.commit()
        db.refresh(instance)

        return instance

    def delete_metric_instance_by_id(self, instance_id, db):
        instance = self.find_metric_instance_by_id(instance_id, db)

        db.delete(instance)
        db.commit()

        return "OK"

    def metric_instance_param_parser(self, req_body):
        """Function to remove "<" and ">" symbol from the request body keys"""
        # req_body look like this
        # req_body = {'<BATCH_ID>': '123456', '<GROUP>': 'TEST_GROUP_NAME', '<ADDRESS_STATE>': 'OHIO'}
        temp_dict = dict()
        custom_parameter_string = ""

        for key in req_body.keys():
            altered_key = key.replace("<", "")  #'BATCH_ID>'
            altered_key = altered_key.replace(">", "")  #'BATCH_ID'
            temp_dict[altered_key] = req_body[
                key
            ]  # temp_dict['BATCH_ID'] = req_body['key']
            if custom_parameter_string != "":
                custom_parameter_string += (
                    ", " + altered_key + ":" + temp_dict[altered_key]
                )
            else:
                custom_parameter_string += altered_key + ":" + temp_dict[altered_key]
        return custom_parameter_string
