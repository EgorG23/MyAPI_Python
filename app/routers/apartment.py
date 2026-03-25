from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.deps import get_current_user
from app.models.user import User
from app.schemas.apartment import ApartmentRequest, ApartmentResponse
from app.services.apartment_service import predict_price, save_prediction

router = APIRouter()


@router.post("/predict", response_model=ApartmentResponse)
def predict(
    request: ApartmentRequest, user: Annotated[User, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)]
):
    predicted_price: float = predict_price(request)

    save_prediction(db=db, data=request, price=predicted_price, user_id=user["id"])

    return ApartmentResponse(predicted_price=predicted_price)
