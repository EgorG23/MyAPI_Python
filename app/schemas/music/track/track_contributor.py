from pydantic import BaseModel, ConfigDict, Field


class TrackContributor(BaseModel):
    role: str = Field(..., max_length=50)


class TrackContributorCreate(TrackContributor):
    track_id: int
    artist_id: int


class TrackContributorResponse(TrackContributor):
    id: int
    track_id: int
    artist_id: int

    model_config = ConfigDict(from_attributes=True)
