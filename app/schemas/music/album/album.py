import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Album(BaseModel):
    spotify_id: str = Field(..., max_length=100)
    title: str = Field(..., max_length=255)
    year: int = Field(..., gt=1600, lt=2027)
    performer: str = Field(..., max_length=200)
    cover_url: Optional[str] = Field(None, max_length=500)
    spotify_url: Optional[str] = Field(None, max_length=500)
    album_type: str = Field(..., pattern="^(album|single|ep)$")


class AlbumCreate(Album):
    pass


class AlbumResponse(Album):
    id: int
    average_overall_point: float = Field(..., ge=0, le=10)
    average_concept_point: float = Field(..., ge=0, le=10)
    average_cover_point: float = Field(..., ge=0, le=10)
    average_visual_point: float = Field(..., ge=0, le=10)
    num_of_reviews: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
