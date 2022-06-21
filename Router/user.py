from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from Router.schemas import UserDisplay, UserBase
from DB.database import get_db
from DB import db_user

router = APIRouter(
    prefix="/user",
    tags = ["user"]
)

@router.post("", response_model = UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db,request)