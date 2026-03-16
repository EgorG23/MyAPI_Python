from fastapi import APIRouter
from schemas.apartment_request import ApartmentRequest
from schemas.apartment_response import ApartmentResponse
from services.predict_price import predict_price, save_prediction
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.post("/predict")
def predict(data: ApartmentRequest, db: Session = Depends(get_db)):
    data_dict = data.dict()
    price = predict_price(data_dict)
    save_prediction(db, data_dict, price)
    return {"predicted_price": price}

