import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TrackBase(BaseModel):
    spotify_id: str = Field(..., max_length=100)
    title: str = Field(..., max_length=255)
    genre: Optional[str] = Field(None, max_length=100)
    tempo: Optional[float] = Field(None, ge=0)
    energy: Optional[float] = Field(None, ge=0, le=1)


class TrackCreate(TrackBase):
    album_id: int


class TrackResponse(TrackBase):
    id: int
    album_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
