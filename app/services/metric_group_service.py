from app.models.models import MdMetricGroup
from fastapi import HTTPException, status


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
        stmt = db.query(MdMetricGroup).filter_by(is_active=True)
        print(f"SQL QUERY: {stmt}")
        groups = stmt.all()
        print(f"MdMetricGroupResultSet: {groups}")
        return groups

    def find_metric_group_by_group_name(self, group_name, db):
        query = (
            db.query(MdMetricGroup)
            .filter_by(md_metric_group_name=group_name)
            .filter_by(is_active=True)
        )
        print(f"SQL QUERY: {query}")
        group = query.first()
        if not group:
            desc = {
                "msg": "Invalid Input",
                "description": f"Group with name: {group_name} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        return group

    def find_metric_group_by_group_id(self, group_id, db):
        query = db.query(MdMetricGroup).filter_by(id=group_id).filter_by(is_active=True)
        print(f"SQL QUERY: {query}")
        group = query.first()
        if not group:
            desc = {
                "msg": "Invalid Input",
                "description": f"Group with name: {group_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        return group

    def update_metric_group_by_group_id(self, group_id, input_body, db):
        query = db.query(MdMetricGroup).filter_by(id=group_id).filter_by(is_active=True)
        print(f"SQL QUERY: {query}")

        group = query.first()
        if not group:
            desc = {
                "msg": "Invalid Input",
                "description": f"Group with id: {group_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)

        for key, value in input_body.items():
            setattr(group, key, value)

        db.add(group)
        db.commit()
        db.refresh(group)

        return group

    def delete_metric_group_by_group_id(self, group_id, db):
        query = db.query(MdMetricGroup).filter_by(id=group_id).filter_by(is_active=True)
        print(f"SQL QUERY: {query}")

        group = query.first()
        if not group:
            desc = {
                "msg": "Invalid Input",
                "description": f"Group with id: {group_id} was not found.",
            }
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=desc)
        db.delete(group)
        db.commit()

        return "OK"
