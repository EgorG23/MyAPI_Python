from datetime import UTC

from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, Text, UniqueConstraint, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class TrackRating(Base):
    __tablename__ = "track_ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey("tracks.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    rating = Column(Float, nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(UTC), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(UTC), onupdate=func.now(UTC), nullable=False)

    track = relationship("Track", back_populates="track_ratings")
    user = relationship("User", back_populates="track_ratings")

    __table_args__ = (
        UniqueConstraint("track_id", "user_id", name="uq_track_user_rating"),
        Index("ix_track_rating_track_id", "track_id"),
        Index("ix_track_rating_user_id", "user_id"),
    )
