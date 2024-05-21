from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models
from .db import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"Home Page"}


@app.get("/test")
def test(db: Session = Depends(get_db())):
    return {"Success": "200"}
