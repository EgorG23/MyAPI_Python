from sqlalchemy.orm import Session

from app.ml_model.model import Prediction_model
from app.models.apartment import Apartment
from app.schemas.apartment import ApartmentRequest

model = Prediction_model()


def predict_price(data: ApartmentRequest) -> float:
    data_dict = data.model_dump()
    return model.predict(data_dict)


def save_prediction(db: Session, data: ApartmentRequest, price: float, user_id: int):
    floor_ratio = data["floor"] / data["num_floors"] if data["num_floors"] else 0
    living_ratio = data["living_area"] / data["total_area"] if data["total_area"] else 0
    apartment = Apartment(
        user_id=user_id,
        housing_type=data["housing_type"],
        district=data["district"],
        rooms=data["rooms"],
        is_studio=data["is_studio"],
        total_area=data["total_area"],
        living_area=data["living_area"],
        kitchen_area=data["kitchen_area"],
        floor=data["floor"],
        num_floors=data["num_floors"],
        bathrooms_type=data["bathrooms_type"],
        num_loggia=data["num_loggia"],
        num_balcony=data["num_balcony"],
        kitchen_and_living=data["kitchen_and_living"],
        condition=data["condition"],
        ceiling_height=data["ceiling_height"],
        nearest_metro_st=data["nearest_metro_st"],
        minutes_to_metro=data["minutes_to_metro"],
        num_freight_lift=data["num_freight_lift"],
        num_passenger_lift=data["num_passenger_lift"],
        parking_type=data["parking_type"],
        building_type=data["building_type"],
        furniture=data["furniture"],
        deal_type=data["deal_type"],
        house_completion_year=data["house_completion_year"],
        first_floor_is_com=data["first_floor_is_com"],
        playground=data["playground"],
        floor_ratio=floor_ratio,
        living_ratio=living_ratio,
        predicted_price=price,
    )
    db.add(apartment)
    db.commit()
    db.refresh(apartment)
    return apartment
