import shutil
from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from Auth.oauth2 import get_current_user
from Router.schemas import PostBase, PostDisplay, UserAuth
from DB.database import get_db
from DB import db_post
from typing import List
import random
import string

router = APIRouter(
    prefix="/post",
    tags = ["post"]
)

image_url_types = ["absolute", "relative"]

@router.post("")
def create(request: PostBase, db: Session = Depends(get_db),current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "parameter image_url_type is wrong")
    return db_post.create(db,request)

@router.get("/all", response_model = List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.post("/image")
def upload_image(image:UploadFile = File(...),current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".",1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}