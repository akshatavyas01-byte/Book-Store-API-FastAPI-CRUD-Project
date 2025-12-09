'''
DAY 1 — Simple FastAPI CRUD (Starter Level)
Problem Statement:
Build a FastAPI CRUD API for a “Book Notes Manager”.
Tech to Use:
FastAPI, Pydantic
Tasks:
✔ Create routes: add, get, update, delete notes
✔ Add try/except around all DB-like operations (in-memory list)
✔ Explain endpoints in README

 '''

from fastapi import FastAPI, Path, Query, Depends
from typing import Annotated
from .models import Book, Updatebook




app=FastAPI()

bookstore={}
book_id=1
@app.post('/books/create_record')
async def create_record(
    book:Book
):
    try:
        global book_id
        bookstore.update({book_id:{**book.model_dump()}})
        create_record=bookstore[book_id]
        response_id=book_id
        book_id+=1
        return f'Record created successfully {response_id} with record {create_record}' 
    except Exception as e:
        return e

@app.get('/books/get_records')
async def get_records():
    try:
        return bookstore
    except Exception as e:
        return e

@app.get('/books/get_record/{book_id}')
async def get_all_records(
    book_id:Annotated[int, Path(title='Book ID',description='Unique Id for the book')]
    ):
    try:
        if book_id in bookstore:
            return bookstore[book_id]
        else:
            return f'No record at {book_id} in bookstore'
    except Exception as e:
        return e
 
@app.put('/books/change_record/{book_id}')
async def change_record(
   book_id:Annotated[int, Path(title='Book ID',description='Unique Id for the book')],
   book:Book,
   q:Annotated[bool,Query(title='Conformation',description='Conformation for Swapping')]=False
):
    try:
        if q:
            if book_id in bookstore:
                updated_record={**book.model_dump()}
                bookstore[book_id].update(updated_record)
                return f'Value replaced at {book_id} with {updated_record}'
            else:
                return f'Book id {book_id} not in bookstore'

    except Exception as e:
        return e
    

@app.patch('/books/update_record/{book_id}')
async def update_record(
    book_id:Annotated[int, Path(title='Book ID',description='Unique Id for the book')],
    update:Updatebook=Depends()
):
    try:
       if book_id in bookstore:
        for key, value in update:
            if value:
                bookstore[book_id][key]=value
        return f'The updated record is {bookstore[book_id]}'
       else:
           return f'Book id {book_id} not in bookstore'
    except Exception as e:
        return e

@app.delete('/books/delete_record/{book_id}')
async def del_record(
 book_id:Annotated[int, Path(title='Book ID',description='Unique Id for the book')],
 q:Annotated[bool,Query(title='Conformation',description='Conformation for deletion')]=False
):
    try:
        if q:
            if book_id in bookstore:
                removed_record=bookstore.pop(book_id)
                return f'Record deleted for {book_id} with {removed_record}'
            else:
                return f'Book id {book_id} not in bookstore'
    except Exception as e:
        return e        

@app.delete("/books/delete_records")
async def delete_all_records(
    q:Annotated[bool,Query(title='Conformation', description='Conformation on all records deletion')]=False
): 
    global book_id
    try:
        if q:
          values=bookstore.copy()
          bookstore.clear()
          book_id=1
          return f'The bookstore with the values:{values} was deleted'
    except Exception as e:
        return e



