from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import LoginRequest, RefreshRequest
from app.services.auth_service import login_user, logout, refresh_access_token, register_user

router = APIRouter()


@router.post("/register")
def register(data: LoginRequest, db: Annotated[Session, Depends(get_db)]):
    return register_user(db, data.email, data.password)


@router.post("/login")
def login(data: LoginRequest, db: Annotated[Session, Depends(get_db)]):
    return login_user(db, data.email, data.password)


@router.post("/refresh")
def refresh(data: RefreshRequest, db: Annotated[Session, Depends(get_db)]):
    return refresh_access_token(db, data.refresh_token)


@router.post("/logout")
def logout_user(data: RefreshRequest, db: Annotated[Session, Depends(get_db)]):
    return logout(db, data.refresh_token)
