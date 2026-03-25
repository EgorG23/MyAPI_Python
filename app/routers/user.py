from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.deps import get_current_user
from app.models.user import User
from app.services.user_service import predictions

router = APIRouter()


@router.get("/user/me")
def get_me(user: Annotated[User, Depends(get_current_user)]):
    return user


@router.get("/user/predictions")
def users_predictions(user: Annotated[User, Depends(get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return predictions(user, db)
