import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AlbumReviewBase(BaseModel):
    overall_rating: float = Field(..., ge=0.0, le=10.0)
    concept_rating: float = Field(..., ge=0.0, le=10.0)
    visual_rating: float = Field(..., ge=0.0, le=10.0)
    cover_rating: float = Field(..., ge=0.0, le=10.0)
    comment: Optional[str] = Field(None, max_length=2000)


class AlbumReviewCreate(AlbumReviewBase):
    album_id: int


class AlbumReviewResponse(AlbumReviewBase):
    id: int
    album_id: int
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
