from datetime import UTC
from typing import List

from sqlalchemy import Column, DateTime, Index, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.music.album.album_contributor import AlbumContributor
from app.models.music.track.track_contributor import TrackContributor


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    spotify_id = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(200), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now(UTC), nullable=False)

    track_contributors: List["TrackContributor"] = relationship(
        "TrackContributor", back_populates="artist", cascade="all, delete-orphan"
    )
    album_contributors: List["AlbumContributor"] = relationship(
        "AlbumContributor", back_populates="artist", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("spotify_id", name="uq_artist_spotify_id"),
        Index("ix_artist_name", "name"),
    )
