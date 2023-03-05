from sqlalchemy import or_
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username_or_uid(db: Session, username: str, uid: str):
    return db.query(models.User).filter(or_(models.User.username == username, models.User.uid == uid)).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username,
                          uid=user.uid, birthday=user.birthday)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
