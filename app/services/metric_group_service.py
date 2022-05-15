from app.models.models import MdMetricGroup


class MdMetricGroupService:
    """
    MdMetricGroupService is the service for MdMetricGroup Table/Entity
    """

    def save_metric_group(self, input_group, db):
        new_group = MdMetricGroup(
            md_metric_group_name=input_group["md_metric_group_name"]
        )
        print(new_group)
        db.add(new_group)
        db.commit()
        db.refresh(new_group)

        return new_group

    def find_all_metric_groups(self, db):
        print("MdMetricGroups fetching..")
        stmt = db.query(MdMetricGroup).filter_by(is_active=True)
        print(stmt)
        groups = stmt.all()
        return groups
