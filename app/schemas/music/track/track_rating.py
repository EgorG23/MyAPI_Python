import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TrackRatingBase(BaseModel):
    rating: float = Field(..., ge=0.0, le=10.0, description="Оценка трека 0-10")
    comment: Optional[str] = Field(None, max_length=2000, description="Комментарий к треку (опционально)")


class TrackRatingCreate(TrackRatingBase):
    track_id: int


class TrackRatingResponse(TrackRatingBase):
    id: int
    track_id: int
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
