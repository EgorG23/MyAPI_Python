from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine
from app.routers.apartment import router as predict_router
from app.routers.auth import router as auth_router
from app.routers.music import router as music_router
from app.routers.user import router as user_router

app = FastAPI(title="MyAPI")

app.include_router(predict_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(music_router)


Base.metadata.create_all(bind=engine)
