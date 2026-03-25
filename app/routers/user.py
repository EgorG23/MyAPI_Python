from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.deps import get_current_user
from app.services.user_service import predictions

router = APIRouter()


@router.get("/user/me")
def get_me(user=Depends(get_current_user)):
    return user


@router.get("/user/predictions")
def users_predicitons(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return predictions(user, db)
