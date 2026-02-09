from pydantic import BaseModel, Field
from typing import Optional
import uuid

class BookRequest(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: Optional[int] = None
    genre: Optional[str] = None

class BookResponse(BaseModel):
    id: uuid.UUID
    title: str 
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None