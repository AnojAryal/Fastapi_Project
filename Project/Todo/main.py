from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, users, address
from company import company_apis
from starlette import status
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Create database tables on startup
models.Base.metadata.create_all(bind=engine)

app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
async def root():
    return RedirectResponse(url='todos',status_code=status.HTTP_302_FOUND)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(users.router)
app.include_router(company_apis.router)