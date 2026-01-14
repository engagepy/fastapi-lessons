from enum import Enum
from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/lesson-1",
    tags=["Lesson 1"]
)

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@router.get(
    "/models/{model_name}",
    summary="Enum path parameter and conditional logic",
    description="Demonstrates Enum usage as a path parameter and conditional branching based on the value."
)
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Getting the hands on AlexNet"}
    if model_name == ModelName.resnet:
        return {"model_name": model_name, "message": "Getting the ResNet model"}
    return {"model_name": model_name, "message": "Getting the LeNet model"}

@router.get(
    "/age/{age}",
    summary="Query parameters with defaults and optionals",
    description="Demonstrates query parameters, default values, optional parameters, and a boolean toggle."
)
async def calculate_age(
    age: int,
    years: int = 50,
    desired: int | None = None,
    activate: bool = True
):
    current_year = datetime.now().year
    future_age = age + years
    future_year = current_year + years

    if desired is not None and activate:
        years_needed = desired - age
        if years_needed > 0:
            future_age = desired
            future_year = current_year + years_needed

    return {"current_age": age, "future_age": future_age, "year": future_year}