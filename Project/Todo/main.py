from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos
from company import company_apis

app = FastAPI()

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(company_apis.router)