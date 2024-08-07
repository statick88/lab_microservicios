from sqlalchemy.orm import Session
from . import models

def get_posts(db: Session, title: str = None, content: str = None):
    query = db.query(models.Post)
    if title:
        query = query.filter(models.Post.title.contains(title))
    if content:
        query = query.filter(models.Post.content.contains(content))
    return query.all()
