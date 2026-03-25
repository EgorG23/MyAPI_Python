from datetime import UTC

from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, Text, UniqueConstraint, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class AlbumReview(Base):
    __tablename__ = "album_reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    overall_rating = Column(Float, nullable=False)
    concept_rating = Column(Float, nullable=False)
    visual_rating = Column(Float, nullable=False)
    cover_rating = Column(Float, nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now(UTC), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(UTC), onupdate=func.now(UTC), nullable=False)

    album = relationship("Album", back_populates="album_reviews")
    user = relationship("User", back_populates="album_reviews")

    __table_args__ = (
        UniqueConstraint("album_id", "user_id", name="uq_album_user_review"),
        Index("ix_album_review_album_id", "album_id"),
        Index("ix_album_review_user_id", "user_id"),
    )
