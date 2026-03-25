from datetime import UTC
from typing import List

from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.music.track.track_contributor import TrackContributor
from app.models.music.track.track_rating import TrackRating


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    spotify_id = Column(String(100), unique=True, nullable=False, index=True)
    title = Column(String(255), nullable=False, index=True)
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="CASCADE"), nullable=False)
    genre = Column(String(100), nullable=True)
    tempo = Column(Float, nullable=True)
    energy = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now(UTC), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(UTC), onupdate=func.now(UTC), nullable=False)

    # Relationships
    album = relationship("Album", back_populates="tracks")
    track_ratings: List["TrackRating"] = relationship(
        "TrackRating", back_populates="track", cascade="all, delete-orphan"
    )
    track_contributors: List["TrackContributor"] = relationship(
        "TrackContributor", back_populates="track", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("spotify_id", name="uq_track_spotify_id"),
        Index("ix_track_title", "title"),
        Index("ix_track_album_id", "album_id"),
    )
