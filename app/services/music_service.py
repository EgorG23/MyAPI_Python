from sqlalchemy.orm import Session

from app.models.music.music import UserAlbumRating, UserTrackRating
from app.schemas.music import AlbumRatingCreate


def save_album_rating_with_tracks(db: Session, user_id: int, data: AlbumRatingCreate):
    album_rating = (
        db.query(UserAlbumRating)
        .filter(UserAlbumRating.user_id == user_id, UserAlbumRating.spotify_album_id == data.spotify_album_id)
        .first()
    )

    if album_rating:
        album_rating.overall_score = data.overall_score
        album_rating.cover_score = data.cover_score
        album_rating.concept_score = data.concept_score
        album_rating.visual_score = data.visual_score
        album_rating.comment = data.album_comment
    else:
        album_rating = UserAlbumRating(
            user_id=user_id,
            spotify_album_id=data.spotify_album_id,
            overall_score=data.overall_score,
            cover_score=data.cover_score,
            concept_score=data.concept_score,
            visual_score=data.visual_score,
            comment=data.album_comment,
        )

    db.add(album_rating)
    db.commit()
    db.refresh(album_rating)

    saved_tracks = []
    for track in data.tracks:
        track_rating = (
            db.query(UserTrackRating)
            .filter(UserTrackRating.user_id == user_id, UserTrackRating.spotify_track_id == track.spotify_track_id)
            .first()
        )

        if track_rating:
            track_rating.score = track.score
            track_rating.comment = track.comment
            track_rating.spotify_album_id = data.spotify_album_id
        else:
            track_rating = UserTrackRating(
                user_id=user_id,
                spotify_album_id=data.spotify_album_id,
                spotify_track_id=track.spotify_track_id,
                score=track.score,
                comment=track.comment,
            )

        db.add(track_rating)
        db.commit()
        db.refresh(track_rating)
        saved_tracks.append(track_rating)

    return {"album": album_rating, "tracks": saved_tracks}


def get_user_album_ratings(db: Session, user_id: int):
    return (
        db.query(UserAlbumRating)
        .filter(UserAlbumRating.user_id == user_id)
        .order_by(UserAlbumRating.created_at.desc())
        .all()
    )


def get_album_ratings_with_tracks(db: Session, user_id: int, spotify_album_id: str):
    album = (
        db.query(UserAlbumRating)
        .filter(UserAlbumRating.user_id == user_id, UserAlbumRating.spotify_album_id == spotify_album_id)
        .first()
    )

    if not album:
        return None

    tracks = (
        db.query(UserTrackRating)
        .filter(UserTrackRating.user_id == user_id, UserTrackRating.spotify_album_id == spotify_album_id)
        .all()
    )

    return {"album": album, "tracks": tracks}
