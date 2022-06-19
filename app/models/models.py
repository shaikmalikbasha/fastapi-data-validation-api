from datetime import datetime

from app.config.db_config import Base
from app.utils.constants import PENDING_STATUS, SUCCESS_STATUS
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    inspect,
)
from sqlalchemy.orm import relationship


class MdMetricNotification(Base):
    __tablename__ = "md_metric_notification"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_notification_type = Column(String)
    md_metric_notification_sender = Column(String)
    md_metric_notification_receiver = Column(String)
    md_metric_notification_content = Column(Text)
    md_metric_notification_status = Column(String)
    md_metric_notification_date_time = Column(DateTime, default=datetime.now())


class MdMetricResult(Base):
    __tablename__ = "md_metric_result"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_instance_id = Column(Integer, nullable=False)
    md_metric_group_name = Column(Text, nullable=False)
    md_metric_query_number = Column(Integer, nullable=False)
    md_metric_query_name = Column(Text, nullable=False)
    md_metric_sql_query = Column(Text, nullable=False)
    md_metric_result_record_number = Column(Integer)
    md_metric_result = Column(Text)
    md_metric_date_time = Column(DateTime, default=datetime.now())


class MdMetricInstance(Base):
    __tablename__ = "md_metric_instance"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_schedule_id = Column(Integer, nullable=True, default=0)
    md_metric_group_name = Column(Text, nullable=False)
    md_metric_instance_custom_paramaters = Column(Text, nullable=False)
    md_metric_instance_status = Column(String, nullable=False, default=PENDING_STATUS)
    md_metric_instance_failure_text = Column(Text, nullable=True)
    md_metric_instance_query_attempt_count = Column(Integer, default=0)
    md_metric_instance_query_complete_count = Column(Integer, default=0)
    md_metric_instance_query_pass_count = Column(Integer, default=0)
    md_metric_instance_date_time = Column(DateTime, default=datetime.now())


class MdMetricGroup(Base):
    __tablename__ = "md_metric_group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_group_name = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=True)

    md_metric_queries = relationship("MdMetricQuery")

    def __repr__(self):
        return str(
            {
                c.key: str(getattr(self, c.key))
                for c in inspect(self).mapper.column_attrs
            }
        )


class MdMetricQuery(Base):
    """
    MdMetricQuery has One-To-One relationship with MdMetricThreshold
    """

    __tablename__ = "md_metric_query"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_query_name = Column(Text, nullable=False)
    md_metric_sql_query = Column(Text, nullable=False)
    md_metric_query_status = Column(String, default=SUCCESS_STATUS)

    md_metric_group_id = Column(Integer, ForeignKey("md_metric_group.id"))
    md_metric_threshold = relationship(
        "MdMetricThreshold", back_populates="md_metric_query"
    )

    def __repr__(self):
        return str(self.__dict__)


class MdMetricThreshold(Base):
    __tablename__ = "md_metric_threshold"

    id = Column(Integer, primary_key=True, autoincrement=True)
    md_metric_threshold_type = Column(String, nullable=False)
    md_metric_threshold_value = Column(Text, nullable=False)
    md_metric_threshold_failure_text = Column(Text)
    md_metric_threshold_action = Column(String)
    md_metric_threshold_action_parameters = Column(Text)
    md_metric_threshold_status = Column(String, default="ACTIVE")

    md_metric_query_id = Column(Integer, ForeignKey("md_metric_query.id"))
    md_metric_query = relationship(
        "MdMetricQuery", back_populates="md_metric_threshold"
    )

    def __repr__(self):
        return str(self.__dict__)
