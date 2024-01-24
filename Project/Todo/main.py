from fastapi import FastAPI, Depends, HTTPException
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


@app.get('/todo/{todo_id}')
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .first()
    
    if todo_model is not None:
        return todo_model
    
    raise http_exception()



def http_exception():
    return HTTPException(status_code=404, detail=f'Todo not found')