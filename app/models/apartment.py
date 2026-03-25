from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.db.base import Base


class Apartment(Base):
    __tablename__ = "apartments"
    user_id = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    housing_type = Column(String, nullable=False)
    district = Column(String, nullable=False)
    rooms = Column(Integer, nullable=False)
    is_studio = Column(String, nullable=False)
    total_area = Column(Float, nullable=False)
    living_area = Column(Float, nullable=False)
    kitchen_area = Column(Float, nullable=False)
    floor = Column(Integer, nullable=False)
    num_floors = Column(Integer, nullable=False)
    bathrooms_type = Column(String, nullable=False)
    num_loggia = Column(Integer, nullable=False)
    num_balcony = Column(Integer, nullable=False)
    kitchen_and_living = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    ceiling_height = Column(Float, nullable=False)
    nearest_metro_st = Column(String, nullable=False)
    minutes_to_metro = Column(Float, nullable=False)
    num_freight_lift = Column(Integer, nullable=False)
    num_passenger_lift = Column(Integer, nullable=False)
    parking_type = Column(String, nullable=False)
    building_type = Column(String, nullable=False)
    furniture = Column(String, nullable=False)
    deal_type = Column(String)
    house_completion_year = Column(String)
    first_floor_is_com = Column(String, nullable=False)
    playground = Column(String, nullable=False)
    floor_ratio = Column(Float, nullable=False)
    living_ratio = Column(Float, nullable=False)
    predicted_price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
