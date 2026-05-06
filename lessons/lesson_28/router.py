from fastapi import APIRouter
from typing import Annotated
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-28",
    tags=["Lesson 28"]
)


class Basket(BaseModel):
    id: int
    name: str
    price: float
    description: str | None = None
    tax: float | None = None
    tags: list[str] = []


@router.post(
    "/items",
    summary="Using Response Model in FastAPI Pydantic Model",
    description="Observe how to use Response Model in FastAPI Pydantic Model"
)
async def create_item(Basket: Basket) -> Basket:
    return Basket

@router.get(
    "/items",
    summary="Using Response Model in FastAPI Pydantic Model",
    description="Observe how to use Response Model in FastAPI Pydantic Model"
)
async def read_items() -> list[Basket]:
    return [
        Basket(
            id=1,
            name="Basket 1",
            price=10.0,
            description="This is the first basket",
            tax=1.0,
            tags=["tag1", "tag2"]
        ),
        Basket(
            id=2,
            name="Basket 2",
            price=20.0,
            description="This is the second basket",
            tax=2.0,
            tags=["tag3", "tag4"]
        )
    ]