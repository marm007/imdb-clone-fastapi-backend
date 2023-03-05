from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    birthday: datetime


class UserCreate(UserBase):
    uid: str


class User(UserBase):
    id: int
    is_active: bool
    confirmed_at: Optional[datetime]

    class Config:
        orm_mode = True
