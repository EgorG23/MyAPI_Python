from sqlalchemy import Column, ForeignKey, Index, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base


class TrackContributor(Base):
    __tablename__ = "track_contributors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    track_id = Column(Integer, ForeignKey("tracks.id", ondelete="CASCADE"), nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id", ondelete="CASCADE"), nullable=False)
    role = Column(String(50), nullable=False)

    track = relationship("Track", back_populates="track_contributors")
    artist = relationship("Artist", back_populates="track_contributors")

    __table_args__ = (
        UniqueConstraint("track_id", "artist_id", "role", name="uq_track_artist_role"),
        Index("ix_track_contributor_track_id", "track_id"),
        Index("ix_track_contributor_artist_id", "artist_id"),
    )
