import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.services.user_service import create_user, get_user_by_email


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = hash_password(password)
    return create_user(db, email, hashed)


def login_user(db: Session, email: str, password: str):
    user: User = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user.email, "role": user.role, "id": user.id})
    refresh_token = str(uuid.uuid4())
    db_token = RefreshToken(token=refresh_token, user_id=user.id)
    db.add(db_token)
    db.commit()
    return {"access_token": access_token, "refresh_token": refresh_token}


def refresh_access_token(db: Session, refresh_token: str):
    db_token = db.query(RefreshToken).filter(RefreshToken.token == refresh_token).first()
    if not db_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    user = db.query(User).filter(User.id == int(db_token.user_id)).first()
    return {"access_token": create_access_token({"sub": user.email, "role": user.role, "id": user.id})}


def logout(db: Session, refresh_token: str):
    db_token = db.query(RefreshToken).filter(RefreshToken.token == refresh_token).first()
    if db_token:
        db.delete(db_token)
        db.commit()
    return {"message": "Logged out"}
