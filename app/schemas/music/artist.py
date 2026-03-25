import datetime

from pydantic import BaseModel, ConfigDict, Field


class ArtistBase(BaseModel):
    spotify_id: str = Field(..., max_length=100)
    name: str = Field(..., max_length=200)


class ArtistCreate(ArtistBase):
    pass


class ArtistResponse(ArtistBase):
    id: int
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
