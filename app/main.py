from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.router.book import book_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )

app.include_router(book_router)