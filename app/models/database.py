import uuid
from sqlmodel import SQLModel, Field
from typing import Optional

class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    author: str
    year: Optional[int] = None
    genre: Optional[str] = None #add genre field