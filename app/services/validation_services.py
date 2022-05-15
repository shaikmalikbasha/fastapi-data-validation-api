from app.models.models import MdMetricInstance, MdMetricQuery, MdMetricThreshold


class ValidationService:
    def get_all_md_instance(self, db):
        return db.query(MdMetricInstance).all()

    def add_queries_for_groups(self, db, args: dict):
        print(f"ARGS: {args}")
        md_metric_query = MdMetricQuery(
            md_metric_group_name=args["md_metric_group_name"],
            md_metric_query_name=args["md_metric_query_name"],
            md_metric_query_number=args["md_metric_query_number"],
            md_metric_sql_query=args["md_metric_sql_query"],
        )
        db.session.add(md_metric_query)
        db.session.commit()
        db.session.refresh(md_metric_query)

        md_metric_threshold = MdMetricThreshold(
            md_metric_group_name=args["md_metric_group_name"],
            md_metric_query_number=args["md_metric_query_number"],
            md_metric_threshold_type=args["md_metric_threshold_type"],
            md_meytric_threshold_value=args["md_meytric_threshold_value"],
            md_metric_threshold_failure_text="",
            md_metric_threshold_action="NOTIFICATION",
            md_metric_threshold_action_parameters="@__shaikmalikbasha__",
            md_metric_threshold_status="ACTIVE",
        )
        db.session.add(md_metric_threshold)
        db.session.commit()
        db.session.refresh(md_metric_threshold)

        return {
            "md_metric": md_metric_query,
            "md_metric_threshold": md_metric_threshold,
        }
