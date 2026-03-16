from database import engine, Base
from models import apartment, log
from fastapi import FastAPI
from routers.predict import router as predict_router

app = FastAPI()

app.include_router(predict_router)

Base.metadata.create_all(bind=engine)
