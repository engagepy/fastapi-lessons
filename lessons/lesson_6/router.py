from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-6",
    tags=["Lesson 6"]
)

@router.get(
    "/items/",
    summary="Multiple query params with validation",
    description="Demonstrates multiple query parameters with uniform validation using FastAPI Query."
)
async def read_items(q: Annotated[list[str] | None, Query(max_length=20)] = None):
    results = {"items": [{"item_name": "Pizza"}, {"toppings": "Basil, Cheese, Tomato Sauce"}]}
    if q:
        results.update({"extras": q})
    return results