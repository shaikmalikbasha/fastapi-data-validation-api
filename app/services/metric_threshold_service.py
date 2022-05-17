from app.models.models import MdMetricThreshold
from fastapi import HTTPException, status


class MdMetricThresholdService:
    """
    MdMetricThresholdService is the service for MdMetricThreshold Table/Entity
    """

    def save_metric_threshold(self, input_body, db):
        new_query = MdMetricThreshold(
            md_metric_threshold_type=input_body["md_metric_threshold_type"],
            md_meytric_threshold_value=input_body["md_meytric_threshold_value"],
            md_metric_threshold_failure_text=input_body[
                "md_metric_threshold_failure_text"
            ],
            md_metric_threshold_action=input_body["md_metric_threshold_action"],
            md_metric_threshold_action_parameters=input_body[
                "md_metric_threshold_action_parameters"
            ],
            md_metric_threshold_status=input_body["md_metric_threshold_status"],
            md_metric_query_id=input_body["md_metric_query_id"],
        )

        db.add(new_query)
        db.commit()
        db.refresh(new_query)

        return new_query

    def find_all_metric_thresholds(self, db):
        thresholds = db.query(MdMetricThreshold).all()
        print(f"MdMetricThresholdResultSet: {thresholds}")

        return thresholds

    def find_metric_threshold_by_id(self, threshold_id, db):
        query = db.query(MdMetricThreshold).filter_by(id=threshold_id)
        print(f"SQL QUERY: {query}")

        metric_threshold = query.first()
        print(f"MdMetricThresholdResult: {metric_threshold}")

        if not metric_threshold:
            desc = {
                "msg": "Invalid Input",
                "description": f"Threshold with id: {threshold_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        return metric_threshold

    def update_metric_threshold_by_id(self, threshold_id, input_body, db):
        metric_threshold = self.find_metric_threshold_by_id(threshold_id, db)
        print(f"MdMetricThresholdResult: {metric_threshold}")

        for key, value in input_body.items():
            setattr(metric_threshold, key, value)

        db.add(metric_threshold)
        db.commit()
        db.refresh(metric_threshold)

        return metric_threshold

    def delete_metric_threshold_by_id(self, threshold_id, db):
        metric_threshold = self.find_metric_threshold_by_id(threshold_id, db)
        print(f"MdMetricThresholdResult: {metric_threshold}")

        db.delete(metric_threshold)
        db.commit()

        return "OK"
