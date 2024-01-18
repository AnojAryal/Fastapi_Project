from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length = 1, max_length = 100)
    description: Optional[str] = Field(
        title="Description of the book",
        max_length=100,
        min_length=1,
        default=None
    )
    rating: int = Field(gt =-1 , lt= 101)

BOOKS  = []


@app.get('/')
async def read_all_books():
    if len(BOOKS) < 1:
        create_book_no_api()
    return BOOKS


@app.post('/')
async def create_book(book : Book):
    BOOKS.append(book)
    return book


def create_book_no_api():
    book_1 = BOOKS(id ='90e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 1', 
                author = 'Author 1', 
                description = 'Description 1', 
                rating = 60 )
    book_2 = BOOKS(id ='80e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 2', 
                author = 'Author 2', 
                description = 'Description 2', 
                rating = 70 )
    book_3 = BOOKS(id ='70e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 3', 
                author = 'Author 3', 
                description = 'Description 3', 
                rating = 80 )
    book_4 = BOOKS(id ='60e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 4', 
                author = 'Author 4', 
                description = 'Description 4', 
                rating = 90 )
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)