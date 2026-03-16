from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class ApiLog(Base):
    __tablename__ = "api_logs"
    id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    response_time = Column(Float)
    status_code = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())


