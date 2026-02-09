from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session, select
from app.models.database import Book
from app.models.engine import get_db
from app.schema.book import BookRequest, BookResponse
import uuid

book_router = APIRouter(tags=["Books"])

@book_router.get("/books", status_code=status.HTTP_200_OK, response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    stmt = select(Book)
    result = db.exec(stmt)
    books = result.all()
    return books

@book_router.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(body: BookRequest, db: Session = Depends(get_db)):
    try:
        new_book = Book(title=body.title, author=body.author, year=body.year)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return {"message": "Book created successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@book_router.get("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=BookResponse)
def get_book(book_id: uuid.UUID, db: Session = Depends(get_db)):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book