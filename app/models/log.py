from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.db.base import Base


class ApiLog(Base):
    __tablename__ = "api_logs"
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    response_time = Column(Float)
    status_code = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
