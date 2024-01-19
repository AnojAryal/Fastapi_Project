from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(
        title="Description of the book",
        max_length=100,
        min_length=1,
        default=None
    )
    rating: int = Field(gt=-1, lt=101)

    class Config:
        json_schema_extra = {
            'example': {
                'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'title': 'Computer Science Pro',
                'author': 'FraNzY',
                'description': 'A very nice Description of book',
                'rating': 75
            }
        }


BOOKS  = []


@app.get('/')
async def read_all_books(books_to_return : Optional[int]= None):
    if len(BOOKS) < 1:
        create_book_no_api()

    if books_to_return and len(BOOKS) >= books_to_return >0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i -1])
            i += 1
        return new_books
    return BOOKS


@app.get('/book/{book_id}')
async def read_book(book_id : UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x



@app.post('/')
async def create_book(book : Book):
    BOOKS.append(book)
    return book


def create_book_no_api():
    book_1 = Book(id ='90e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 1', 
                author = 'Author 1', 
                description = 'Description 1', 
                rating = 60 )
    book_2 = Book(id ='80e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 2', 
                author = 'Author 2', 
                description = 'Description 2', 
                rating = 70 )
    book_3 = Book(id ='70e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 3', 
                author = 'Author 3', 
                description = 'Description 3', 
                rating = 80 )
    book_4 = Book(id ='60e571fb-6083-4668-9aba-919d59aa878f', 
                title = 'Title 4', 
                author = 'Author 4', 
                description = 'Description 4', 
                rating = 90 )
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)