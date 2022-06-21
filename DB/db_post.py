from fastapi import HTTPException, status
from Router.schemas import PostBase
from sqlalchemy.orm.session import Session
from DB.models import DbPost
import datetime

def create(db: Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url, 
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestmap = datetime.datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db:Session):
    return db.query(DbPost).all()

def delete(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id ${id} not found")
    
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"only post creator can delete post")
    
    db.delete(post)
    db.commit()
    return "OK"