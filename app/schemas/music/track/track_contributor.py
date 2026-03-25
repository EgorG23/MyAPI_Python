from pydantic import BaseModel, ConfigDict, Field


class TrackContributorBase(BaseModel):
    role: str = Field(..., max_length=50)


class TrackContributorCreate(TrackContributorBase):
    track_id: int
    artist_id: int


class TrackContributorResponse(TrackContributorBase):
    id: int
    track_id: int
    artist_id: int

    model_config = ConfigDict(from_attributes=True)
