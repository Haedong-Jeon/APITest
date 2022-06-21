from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from Router.schemas import PostBase, PostDisplay
from DB.database import get_db
from DB import db_post
from typing import List

router = APIRouter(
    prefix="/post",
    tags = ["post"]
)

image_url_types = ["absolute", "relative"]

@router.post("")
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "parameter image_url_type is wrong")
    return db_post.create(db,request)

@router.get("/all", response_model = List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)
