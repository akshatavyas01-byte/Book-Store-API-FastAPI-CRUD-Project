# Book Store API – FastAPI CRUD Project

A simple **FastAPI CRUD API** for managing books, built as the first project in my learning series.

It performs *Create, Read, Update, and Delete (CRUD)* operations for handling book records.

---
## Features
1. CRUD OPERATIONS:
    - Create book record *(POST)*
    - Read book records or a specific record *(GET)*
    - Update the full record or a specific section *(PUT/PATCH)*
    - Delete all records or sepcific record *(DELETE)*

2. FAST API CONCEPTS:
    - Path parameters
    - Query parameters
    - Pydantic models for validation
    - Annotated typing
    - Auto docs (Swagger UI)

3. PROJECT ARCHITECTURE
    - In-memory list temporary data storage 
    - Seperate file for pydantic models
    - requests/ folder for HTTP request testing

4.  TESTING
    - POSTMAN
    - Python Requests

----
## Technologies Used
    Python 3.x  
    Uvicorn  
    Pydantic  
    Requests
---
## Folder Structure
    project/
        |── src/
        |  |── main.py
        |  └── models.py
        |
        |── requests/
        |   |── delete_all.py
        |   |── delete_record.py
        |   |── get_all.py
        |   |── get_record.py
        |   |── patch_record.py
        |   |── post_record.py
        |   |── post_record2.py
        |   └── put_record.py
        |
        |── images/
        |
        |── requirements.txt
        |
        └── ReadMe.md

---

## Installation & Setup for the project

```python
git clone <your repo>
cd project-name

pip install -r requirements.txt

uvicorn main:app --reload

```
---
## Environment Setup
```python

python -m venv venv

venv/Scripts/Activate.ps1

```
## Install Dependencies
```python

pip install -r requirements.txt

```
---
## API Endpoints

| Method | Endpoint | Parameters| Description |
|--------|----------|--|-----------|
| POST   | /books/create_record |Body(JSON)|Creates a new book record|
| GET | /books/get_records | None | Retrieves all book records
| GET | /books/get_record/{book_id} |Path: **id** | Retrieves the record of the specified book
| PUT | /books/change_record/{book_id}|Path: **id**, **q:** (bool-Confirmation), Body(JSON) | Updates the entire record
| PATCH | /books/update_record/{book_id}| Path: **id**, Query: **Fields of Updatebook model**| Updates specific fields of the record
|DELETE| /books/delete_record/{book_id}|Path: **id**, **q:**(bool-Confirmation)| Deletes the specified record
|DELETE|/books/delete_records| **q:**(bool-Confirmation)| Deletes all records


----

## Request Example
**POST JSON** 
```json
{
    'title':'Pride and Prejudice',
    'author':'Jane Austen',
    'pages':279,
    'publisher':'T. Egerton, Whitehall',
    'published_date':'1813-01-28'
}
```
---

## Demo Images
### Uvicorn Model
![alt text](/images/image.png)

### Swagger UI (docs)
![alt text](/images/image-2.png)
![alt text](/images/image-3.png)
![alt text](/images/image-4.png)

### Swagger UI Post Tryout
![alt text](/images/image-6.png)
![alt text](/images/image-7.png)

### Postman collection overview
![alt text](/images/image-8.png)

### Postman POST
![alt text](/images/image-9.png)

### Postman GET
![alt text](/images/image-10.png)

### Postman PUT
![alt text](/images/image-11.png)

### Postman PATCH
![alt text](/images/image-12.png)

### Postman DELETE 
![alt text](/images/image-13.png)

### Python Post request
![alt text](/images/image-14.png)

---

## License
This project is licensed under the MIT License.

## Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)