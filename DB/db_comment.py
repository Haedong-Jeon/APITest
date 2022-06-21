from datetime import datetime
from fastapi import Depends
from sqlalchemy.orm import Session
from DB.database import get_db
from DB.models import DbComment
from Router.schemas import CommentBase

def create(db:Session, request: CommentBase):
    new_comment = DbComment(
       text = request.text,
       username = request.username,
       post_id = request.post_id,
       timestamp = datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(post_id:int, db: Session):
    return db.query(DbComment).filter(DbComment.post_id == post_id).all()