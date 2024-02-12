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