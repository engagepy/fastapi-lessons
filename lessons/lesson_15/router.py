from typing import Annotated
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum


router = APIRouter(
    prefix="/lesson-15",
    tags=["Lesson 15"]
)


class Item(BaseModel):
    name : str = Field(default="Sample Item", example="Book", max_length=100)
    price : float = Field(default=0.00, example=19.99, ge=0)
    description : str | None = Field(default="A sample item for demonstration", example="A great book about FastAPI", max_length=300)  
    tax : float = Field(default=0.0, example=1.99, ge=0)
    tags : list[str] = Field(default=["sample", "item"], example=["book", "fastapi", "python"]) 

@router.post(
        "/items/{item_id}",
        summary="Create an Item with Path and Body Parameters",
        description="Demonstrates how to use deeply nested Pydantic models in the request body while also accepting path parameters for creating an item",
        )
async def create_item(
    item_id: Annotated[int, Path(title="Item ID", description="The ID of the item to create", gt=0)],
    item: Annotated[Item, Body(title="Item", description="The details of the item to create")]
):
    return {
        "item_id": item_id,
        "item": item.model_dump()
    }

