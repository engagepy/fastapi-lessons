from typing import Annotated
from pydantic import AfterValidator
from fastapi import APIRouter, Query, Path
import enum
import random


router = APIRouter(
    prefix="/lesson-10",
    tags=["Lesson 10"])

@router.post(
    "/cart/{user_id}/item/{item_id}",
    summary="Path parameters numeric validation and metadata using Path",
    description="Demonstrates path parameter numeric validation using Path class."
    )
async def cart_items(
    user_id: Annotated[str, Path(title="Alphanumeric User ID", min_length=5, max_length=15)],
    item_id: Annotated[int, Path(title="Item ID", ge=1, le=4)],
    q: Annotated[str, Query(title="Special instructions for the item", max_length=50)] | None = None
):
    return {"user_id": user_id, "item_id": item_id, "q": q}