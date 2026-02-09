# Books API

A RESTful API built with FastAPI, SQLModel, and Alembic for managing a book library.

## Features

- Create new books with title, author, year, and genre
- Retrieve all books
- Retrieve a specific book by ID
- SQLite database with Alembic migrations
- Interactive API documentation with Swagger UI and Scalar
- Input validation with Pydantic

## Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLModel** - SQL database ORM combining SQLAlchemy and Pydantic
- **Alembic** - Database migration tool
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## Installation
Clone the repository

Bash
git clone [https://github.com/rafliogun49/assignment1.git](https://github.com/rafliogun49/assignment1.git)
cd assignment1
Create virtual environment and install dependencies

Bash
uv venv
uv sync --active
Run database migrations

Bash
uv run alembic upgrade head

## Running the Server
Bash
uv run uvicorn app.main:app --reload
The API will be available at http://localhost:8000
