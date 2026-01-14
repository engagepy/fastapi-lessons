from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-4",
    tags=["Lesson 4"]
)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@router.put(
    "/items/{item_id}",
    summary="Request body with Pydantic model",
    description="Demonstrates request body parameters using a Pydantic model together with path and query parameters."
)
async def update_item(
    item_id: int,
    item: Item,
    q: str | None = None
):
    result = {"item_id": item_id, "item": item}
    if q:
        result.update({"q": q})
    return result