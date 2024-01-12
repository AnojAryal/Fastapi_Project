from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
# import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit: int = 10, published: bool = False,sort :Optional[str]=None):
    # only get 10 published blogs by default
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}



@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id
    return {'data': {'1', '2'}}

#creating the Blog model
class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]
       

@app.post('/blog')
#using blog model
def create_blog(blog:Blog):
    return {'data':f"Blog is created with title as {blog.title}"} #getting values



#for debugging 
# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)