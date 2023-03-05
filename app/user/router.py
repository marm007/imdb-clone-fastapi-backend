from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from . import schemas, service

router = APIRouter()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_username_or_uid(
        db, username=user.username, uid=user.uid)
    if db_user:
        error_message = "Something went wrong"
        if db_user.uid == user.uid:
            error_message = "UID already registered"
        elif db_user.username == user.username:
            error_message = "Username already registred"
        raise HTTPException(status_code=400, detail=error_message)
    return service.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def get_all_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    users = service.get_all_users(db)
    return users
