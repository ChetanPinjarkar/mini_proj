from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Read the root endpoint."""
    return {"message": "Hello, FastAPI is running!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Read an item by its ID."""
    return {"item_id": item_id, "q": q}