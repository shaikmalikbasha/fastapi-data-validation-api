from app.models.models import MdMetricQuery
from app.utils.constants import SUCCESS_STATUS
from fastapi import HTTPException, status


class MdMetricQueryService:
    """
    MdMetricQueryService is the service for MdMetricQuery Table/Entity
    """

    def save_metric_query(self, input_group, db):
        new_query = MdMetricQuery(
            md_metric_query_name=input_group["md_metric_query_name"],
            md_metric_sql_query=input_group["md_metric_sql_query"],
            md_metric_query_status=input_group["md_metric_query_status"],
            md_metric_group_id=input_group["md_metric_group_id"],
        )
        print(new_query)
        db.add(new_query)
        db.commit()
        db.refresh(new_query)

        return new_query

    def find_all_metric_queries(self, db):
        stmt = db.query(MdMetricQuery).filter_by(md_metric_query_status=SUCCESS_STATUS)
        print(f"SQL QUERY: {stmt}")
        groups = stmt.all()
        print(f"MdMetricQUeryResultSet: {groups}")
        return groups

    def find_metric_query_by_id(self, query_id, db):
        query = (
            db.query(MdMetricQuery)
            .filter_by(id=query_id)
            .filter_by(md_metric_query_status=SUCCESS_STATUS)
        )
        print(f"SQL QUERY: {query}")
        metric_query = query.first()
        print(f"MdMetricQueryResult: {metric_query}")
        if not metric_query:
            desc = {
                "msg": "Invalid Input",
                "description": f"Query with id: {query_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        return metric_query

    def update_metric_query_by_id(self, query_id, input_body, db):
        metric_query = self.find_metric_query_by_id(query_id, db)
        print(f"MdMetricQueryResult: {metric_query}")

        for key, value in input_body.items():
            setattr(metric_query, key, value)

        db.add(metric_query)
        db.commit()
        db.refresh(metric_query)

        return metric_query

    def delete_metric_query_by_id(self, query_id, db):
        metric_query = self.find_metric_query_by_id(query_id, db)
        print(f"MdMetricQueryResult: {metric_query}")

        db.delete(metric_query)
        db.commit()

        return "OK"
