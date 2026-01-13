from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI(title="Lesson 4 - Request Body Parameters with Pydantic", version="1.0.0", description="An example FastAPI application demonstrating body + path + query parameters")

@app.put("/items/{item_id}", tags=["Observe request body parameters using Pydantic Model along with path and query parameters"])
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, "item": item}
    if q:
        result.update({"q": q})
    return result

