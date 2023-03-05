from .database import Base, engine
from fastapi import FastAPI

from .user import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router.router)
