from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal

app = FastAPI()

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
async def read_all(db: Session = Depends(get_db)):
    # Query all Todos from the database
    todos = db.query(models.Todos).all()
    return todos
