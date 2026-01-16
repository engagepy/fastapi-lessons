from typing import Annotated
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/lesson-7",
    tags=["Lesson 7"]
)

@router.get(
    "/bike_service/",
    summary="Multiple query params with validation",
    description="Demonstrates query metadata addition using title, alias, and max_length using Query class."
)
async def bike_repair(
    q: Annotated[list[str] | None, 
                 Query(
                     title= "Observations on bike", 
                     max_length=20, alias="bike-damage")] = None
                     ): # just list use is possible, no str
    results = {"items": [{"number": "HR01X"}, {"service_needs": "Oil Change, Tire Rotation"}]}
    if q:
        results.update({"observations": q})
    return results