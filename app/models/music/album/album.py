from datetime import UTC
from typing import List

from sqlalchemy import Column, DateTime, Float, Index, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.music.album.album_contributor import AlbumContributor
from app.models.music.album.album_review import AlbumReview
from app.models.music.track.track import Track


class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    spotify_id = Column(String(100), unique=True, nullable=False, index=True)
    title = Column(String(255), nullable=False, index=True)
    year = Column(Integer, nullable=False)
    performer = Column(String(200), nullable=False)
    cover_url = Column(String(500), nullable=True)
    spotify_url = Column(String(500), nullable=True)
    album_type = Column(String(20), nullable=False, default="album")
    average_overall_point = Column(Float, nullable=False, default=0.0)
    average_concept_point = Column(Float, nullable=False, default=0.0)
    average_cover_point = Column(Float, nullable=False, default=0.0)
    average_visual_point = Column(Float, nullable=False, default=0.0)
    num_of_reviews = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, server_default=func.now(UTC), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(UTC), onupdate=func.now(UTC), nullable=False)

    tracks: List["Track"] = relationship("Track", back_populates="album", cascade="all, delete-orphan")
    album_reviews: List["AlbumReview"] = relationship(
        "AlbumReview", back_populates="album", cascade="all, delete-orphan"
    )
    album_contributors: List["AlbumContributor"] = relationship(
        "AlbumContributor", back_populates="album", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("spotify_id", name="uq_album_spotify_id"),
        Index("ix_album_title_year", "title", "year"),
        Index("ix_album_performer", "performer"),
    )
