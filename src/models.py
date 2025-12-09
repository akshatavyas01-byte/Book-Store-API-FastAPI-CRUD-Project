from pydantic import BaseModel, Field
from datetime import date

class Book(BaseModel):
    title:str = Field(title='Title', description='Name of the books', max_length=50)
    author: str | None = Field(default='Anoynonmus',title='Author', description='Name of the author', max_length=50) 
    description:str|None=Field(default=None,title='Description',description='Description of the book', max_length=500)
    pages: int=Field(title='Number of pages', description='Length of book' )
    publisher:str|None=Field(default='Anoynonmus',title='Publisher', description='Name of the book Publisher', max_length=70)
    published_date:date| None =Field(default=None, title='Publishing date',description='Date of book publishing')

class Updatebook(BaseModel):
    title:str |None=Field(None,title='Update Title', description='Update Name of the books', max_length=50)
    author: str | None = Field(None,title='Update Author', description='Update Name of the author', max_length=50) 
    description:str|None=Field(None,title='Update Description',description='Update Description of the book', max_length=500)
    pages: int|None =Field(None,title='Update Number of pages', description='Update Length of book' )
    publisher:str|None=Field(None,title='Update Publisher', description='Update Name of the book Publisher', max_length=70)
    published_date:date| None =Field(None,title='Update Publishing date',description='Update Date of book publishing')
