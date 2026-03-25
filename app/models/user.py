from datetime import UTC, datetime
from typing import List

from sqlalchemy import Column, DateTime, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.music.album.album_review import AlbumReview
from app.models.music.track.track_rating import TrackRating


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC))
    role = Column(String, default="user")

    track_ratings: List["TrackRating"] = relationship(
        "TrackRating", back_populates="user", cascade="all, delete-orphan"
    )
    album_reviews: List["AlbumReview"] = relationship(
        "AlbumReview", back_populates="user", cascade="all, delete-orphan"
    )

    __table_args__ = (UniqueConstraint("username", name="uq_user_username"),)
