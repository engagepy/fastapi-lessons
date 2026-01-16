from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-4",
    tags=["Lesson 4"]
)

class Movies(BaseModel):
    name: str
    description: str | None = None
    part: int | None = 1
    timeline: float | None = None

@router.put(
    "/movie/{movie_id}",
    summary="Request body with Pydantic model",
    description="Demonstrates request body parameters using a Pydantic model together with path and query parameters."
)
async def update_movie(
    movie_id: int,
    movie: Movies,
    query: str | None = None
):
    result = {"movie_id": movie_id, "movie": movie}
    if query:
        result.update({"query": query})
    return result