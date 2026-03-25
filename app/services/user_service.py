import logging

from sqlalchemy.orm import Session

from app.models.apartment import Apartment
from app.models.user import User

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def create_user(db: Session, email: str, hashed_password: str):
    user = User(email=email, hash_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def predictions(user: User, db: Session):
    logging.info(f"JWT payload: {user}")
    apartments_all = db.query(Apartment).all()
    logging.info(f"Все квартиры в БД: {apartments_all}")
    apartments_filtered = db.query(Apartment).filter(Apartment.user_id == int(user["id"])).all()
    logging.info(f"Фильтр по user_id={user['id']}: {apartments_filtered}")
    return db.query(Apartment).filter(Apartment.user_id == int(user["id"])).all()
