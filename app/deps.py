from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.security import decode_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token") from e


def require_role(required_role: str):
    def role_checker(user: Annotated[User, Depends(get_current_user)]):
        if user.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user

    return role_checker
