from sqlalchemy import Column, String, DateTime, Float, Index
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel


class Learning(BaseModel):
    __tablename__ = 'learning'
    __table_args__ = (
        Index('idx_learning_email', 'email'),
        Index('idx_learning_associate_id', 'associate_id'),
        {'schema': 'cdp_tables'}
    )

    associate_id = Column(UUID(as_uuid=True), nullable=False)
    email = Column(String(255), nullable=False)
    skill_name = Column(String(255), nullable=False)
    learning_resource = Column(String(255), nullable=False)
    resource_link = Column(String(255), nullable=False)
    duration = Column(Float, nullable=False)
    start_datetime = Column(DateTime(timezone=True))
    end_datetime = Column(DateTime(timezone=True))
    status = Column(String(255), nullable=False)
