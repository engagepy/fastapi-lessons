from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-5",
    tags=["Lesson 5"]
)

@router.get(
    "/pizza/",
    summary="Query parameter validation",
    description="Demonstrates query parameter validation using FastAPI's Query class."
)
async def pizza(q: Annotated[str | None, Query(max_length=20)] = None):
    results = {
        "items": [
            {"item_name": "Pizza"},
            {"toppings": "Basil, Cheese, Tomato Sauce"},
        ]
    }
    if q:
        results.update({"extras": q})
    return results