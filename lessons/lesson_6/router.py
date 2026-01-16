from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-6",
    tags=["Lesson 6"]
)

@router.get(
    "/pizza/",
    summary="Multiple query parameters with uniform validation using Query class",
    description="Demonstrates multiple query parameters with uniform validation using FastAPI Query."
)
async def pizza(q: Annotated[list[str] | None, Query(max_length=20)] = None):
    results = {"order": [{"item_name": "Pizza"}, {"toppings": "Basil, Cheese, Tomato Sauce"}]}
    if q:
        results.update({"extras": q})
    return results