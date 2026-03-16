from pydantic import BaseModel, NonNegativeFloat


class ApartmentResponse(BaseModel):
    predicted_price: NonNegativeFloat
