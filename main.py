from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


BOOKS = {
    'book_1': {'title':'Title_1','author': 'Author_1'},
    'book_2': {'title':'Title_2','author': 'Author_2'},
    'book_3': {'title':'Title_3','author': 'Author_3'},
    'book_4': {'title':'Title_4','author': 'Author_4'},
    'book_5': {'title':'Title_5','author': 'Author_5'},
}

class DirectionName(str , Enum):
    north = 'North'
    south = 'South'
    east = 'East'
    west = 'West'

#Query Parameters
@app.get("/")
async def books(skip_book :Optional[str]= None):
    if skip_book: 
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

# enhancing path parameters
@app.get('/{book_name}')
async def read_book(book_name : str):
    return BOOKS[book_name]

@app.get("/book/{book_title}")
async def read_book(book_title):
    return {'Book Title': book_title}


@app.get("/book_id/{book_id}")
async def read_book(book_id: int):
    return {'Book Id': book_id}

#Enumeration path parameters
@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {'Direction': direction_name, 'sub':'Up'}
    if direction_name == DirectionName.south:
        return {'Direction': direction_name, 'sub':'Down'}
    if direction_name == DirectionName.east:
        return {'Direction': direction_name, 'sub':'Left'}
    return {'Direction': direction_name, 'sub':'Right'}