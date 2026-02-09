from sqlmodel import create_engine, SQLModel, Session
from fastapi import Depends

#SQLite database file path
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create engine (connection to database)
engine = create_engine(sqlite_url, echo=True)

def get_db():
    with Session(engine) as session:
        yield session