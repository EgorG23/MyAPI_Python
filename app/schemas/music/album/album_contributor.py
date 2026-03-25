from pydantic import BaseModel, ConfigDict, Field


class AlbumContributor(BaseModel):
    role: str = Field(..., max_length=50)


class AlbumContributorCreate(AlbumContributor):
    album_id: int
    artist_id: int


class AlbumContributorResponse(AlbumContributor):
    id: int
    album_id: int
    artist_id: int

    model_config = ConfigDict(from_attributes=True)
