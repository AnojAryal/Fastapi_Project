import sys
sys.path.append("..")


from fastapi import Depends, APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception, verify_password, get_password_hash


router = APIRouter(
    prefix= '/users',
    tags=['users'],
    responses={404: {'Description': 'Not found'}}
)


models.Base.metadata.create_all(bind = engine)

# Dependency to get a database sessions
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get('/user/{user_id}')
async def user_by_path(user_id: int,db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id ==user_id).first()
    if user_model is not None:
        return user_model
    return 'Invalid user id'
