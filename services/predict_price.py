import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from models.apartment import Apartment
import pickle
from pytorch_tabnet.tab_model import TabNetRegressor

from schemas.apartment_request import ApartmentRequest

with open("scaler_X.pkl", "rb") as f:
    scaler_X = pickle.load(f)
with open("scaler_y.pkl", "rb") as f:
    scaler_y = pickle.load(f)
with open("feature_order.pkl", "rb") as f:
    feature_order = pickle.load(f)

model = TabNetRegressor()
model.load_model("tabnet_model.zip")


def predict_price(data):
    df = pd.DataFrame([data])
    df["floor_ratio"] = df["floor"] / df["num_floors"].replace(0, 1)
    df["living_ratio"] = df["living_area"] / df["total_area"].replace(0, 1)
    df = pd.get_dummies(df)
    for col in feature_order:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_order]
    X_scaled = scaler_X.transform(df)
    pred_scaled = model.predict(X_scaled).flatten()
    pred_price = scaler_y.inverse_transform(pred_scaled.reshape(-1, 1)).flatten()[0]
    return float(pred_price)


def save_prediction(db: Session, data, price: float):
    floor_ratio = data["floor"] / data["num_floors"] if data["num_floors"] else 0
    living_ratio = data["living_area"] / data["total_area"] if data["total_area"] else 0
    apartment = Apartment(
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
        predicted_price=price
    )
    db.add(apartment)
    db.commit()
    db.refresh(apartment)
    return apartment
