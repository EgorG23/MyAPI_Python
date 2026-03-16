from sqlalchemy import Column, Integer, Float, DateTime, String
from sqlalchemy.sql import func
from database import Base


class Apartment(Base):
    __tablename__ = "apartments"
    id = Column(Integer, primary_key=True)
    housing_type = Column(String)
    district = Column(String)
    rooms = Column(Integer)
    is_studio = Column(String)
    total_area = Column(Float)
    living_area = Column(Float)
    kitchen_area = Column(Float)
    floor = Column(Integer)
    num_floors = Column(Integer)
    bathrooms_type = Column(String)
    num_loggia = Column(Integer)
    num_balcony = Column(Integer)
    kitchen_and_living = Column(String)
    condition = Column(String)
    ceiling_height = Column(Float)
    nearest_metro_st = Column(String)
    minutes_to_metro = Column(Float)
    num_freight_lift = Column(Integer)
    num_passenger_lift = Column(Integer)
    parking_type = Column(String)
    building_type = Column(String)
    furniture = Column(String)
    deal_type = Column(String)
    house_completion_year = Column(String)
    first_floor_is_com = Column(String)
    playground = Column(String)
    floor_ratio = Column(Float)
    living_ratio = Column(Float)
    predicted_price = Column(Float)
    created_at = Column(DateTime, server_default=func.now())