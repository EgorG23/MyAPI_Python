from sqlalchemy import Column, ForeignKey, Index, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base import Base


class AlbumContributor(Base):
    __tablename__ = "album_contributors"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="CASCADE"), nullable=False)
    artist_id = Column(Integer, ForeignKey("artists.id", ondelete="CASCADE"), nullable=False)
    role = Column(String(50), nullable=False)

    album = relationship("Album", back_populates="album_contributors")
    artist = relationship("Artist", back_populates="album_contributors")

    __table_args__ = (
        UniqueConstraint("album_id", "artist_id", "role", name="uq_album_artist_role"),
        Index("ix_album_contributor_album_id", "album_id"),
        Index("ix_album_contributor_artist_id", "artist_id"),
    )
