# Assignment 1 Recap: Books API

## What We Built

A **Books API** using FastAPI + SQLModel + Alembic with 2 endpoints:
- `GET /books` — Get all books
- `POST /books` — Create a new book

---


## Project Structure

```
assignment1/
├── alembic/
│   ├── versions/                  # Migration files (database history)
│   │   ├── 8f1508cd8e6f_create_book_table.py
│   │   └── 29beeec0d7fb_add_genre_to_book.py
│   └── env.py                     # Connects Alembic to our models
├── app/
│   ├── models/
│   │   ├── database.py            # Book model (database table blueprint)
│   │   └── engine.py              # Database connection + session
│   ├── router/
│   │   └── book.py                # API endpoints (GET + POST /books)
│   ├── schema/
│   │   └── book.py                # Request/Response validation
│   └── main.py                    # FastAPI app entry point
├── alembic.ini                    # Alembic config (database URL)
├── pyproject.toml                 # Project dependencies
└── database.db                    # SQLite database file
```

---

## Key Concepts We Learned

### 1. FastAPI
- A Python web framework that turns functions into API endpoints
- `@app.get("/books")` = when someone visits `/books`, run this function
- Auto-generates interactive API docs (Swagger UI at `/docs`, Scalar at `/scalar`)

### 2. SQLModel (ORM)
- Lets you work with databases using Python classes instead of raw SQL
- Combines **SQLAlchemy** (database ORM) + **Pydantic** (data validation)
- `table=True` means "this class = a database table"

```python
class Book(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    author: str
```

### 3. Alembic (Database Migrations)
- Version control for your database schema (like git for databases)
- Auto-detects model changes and generates migration files
- Commands:
  - `alembic revision --autogenerate -m "message"` = create a migration
  - `alembic upgrade head` = apply all migrations
  - `alembic downgrade -1` = roll back last migration

### 4. Schemas (Pydantic)
- Separate from database models
- **BookRequest** = what the client sends (no `id`, the database generates it)
- **BookResponse** = what the API returns (includes `id`)
- Types must match! (UUID in model = UUID in schema, not str)

### 5. Dependency Injection
- `Depends(get_db)` = FastAPI automatically provides a database session
- Like a waiter bringing you what you need, instead of going to the kitchen yourself

### 6. Engine & Session
- **Engine** = connection to the database (like a phone)
- **Session** = a conversation with the database (like a phone call)
- `db.add()` = add data, `db.commit()` = save, `db.refresh()` = reload

---

## How Data Flows

```
Client sends POST /books:
  { "title": "Harry Potter", "author": "J.K. Rowling" }
      |
      v
BookRequest validates the data
      |
      v
Router creates a Book object and saves to database
      |
      v
Database generates UUID for id
      |
      v
Client receives 201 Created:
  { "message": "Book created successfully" }
```

```
Client sends GET /books:
      |
      v
Router queries database: SELECT * FROM book
      |
      v
BookResponse filters each book (only returns defined fields)
      |
      v
Client receives 200 OK:
  [{ "id": "abc-123", "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genre": null }]
```

---

## Common Issues We Encountered & Solved

| Issue | Cause | Solution |
|-------|-------|----------|
| Red squiggly lines in VS Code | VS Code using wrong Python interpreter | Select `.venv` interpreter + `uv sync --active` |
| `Can't load plugin: sqlalchemy.dialects:driver` | `alembic.ini` had default URL | Change to `sqlite:///database.db` |
| `NameError: name 'sqlmodel' is not defined` | Auto-generated migration missing import | Add `import sqlmodel` to migration file |
| `ImportError: cannot import name` | Stale `__pycache__` files | Delete `__pycache__` folders |
| `Input should be a valid string` (UUID error) | `BookResponse.id` was `str`, but database returns `UUID` | Change to `id: uuid.UUID` in schema |

---

## Useful Commands

```bash
# Run the server
uv run uvicorn app.main:app --reload

# Create a new migration after changing models
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Roll back last migration
uv run alembic downgrade -1

# Install a new package
uv add package-name

# Sync packages to .venv
uv sync --active
```

---

## URLs

- API Root: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- Scalar Docs: http://localhost:8000/scalar
