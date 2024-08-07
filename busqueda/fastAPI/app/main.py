from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts/", response_model=list[schemas.Post])
def buscar(title: str = None, content: str = None, db: Session = Depends(get_db)):
    return crud.get_posts(db, title=title, content=content)
