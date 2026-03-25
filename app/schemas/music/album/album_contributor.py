from pydantic import BaseModel, ConfigDict, Field


class AlbumContributorBase(BaseModel):
    role: str = Field(..., max_length=50)


class AlbumContributorCreate(AlbumContributorBase):
    album_id: int
    artist_id: int


class AlbumContributorResponse(AlbumContributorBase):
    id: int
    album_id: int
    artist_id: int

    model_config = ConfigDict(from_attributes=True)
