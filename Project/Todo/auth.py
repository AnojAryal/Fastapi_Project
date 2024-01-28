from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
import models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal, engine

class CreateUser(BaseModel):
    username: str
    email:Optional[str]
    first_name:str
    last_name:str
    password: str


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated= 'auto')


# Create database tables on startup
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency to get a database sessions
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_password_hash(password):
    return bcrypt_context.hash(password)


@app.post('/create/user')
async def create_new_user(create_user: CreateUser, db:Session = Depends(get_db)):
    create_user_model = models.Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name


    hashed_password = get_password_hash(create_user.password)

    create_user_model.hashed_password = hashed_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()

    return 'successful'