from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


BOOKS = {
    'book_1': {'title':'Title_1','author': 'Author_1'},
    'book_2': {'title':'Title_2','author': 'Author_2'},
    'book_3': {'title':'Title_3','author': 'Author_3'},
}

@app.get("/")
async def books():
    return BOOKS


@app.get("/book/{book_title}")
async def read_book(book_title):
    return {'Book Title': book_title}


@app.get("/book_id/{book_id}")
async def read_book(book_id: int):
    return {'Book Id': book_id}