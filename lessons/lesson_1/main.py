from enum import Enum
from fastapi import FastAPI
import datetime

app = FastAPI(title="Lesson 1 - Path & Query Parameters", version="1.0.0", description="An example FastAPI application demonstrating path and query parameters.")

# To run the application, use the command: `uvicorn main:app --reload`

# Define an enumeration for model names to restrict valid input values in path parameters

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Define a route that uses the ModelName enumeration as a path parameter

@app.get("/models/{model_name}", tags=["Note the Enum usage, path parameter and conditional logic"])
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Getting the hands on AlexNet"}
    elif model_name.value == "resnet":
        return {"model_name": model_name, "message": "Getting the ResNet modelz"}
    return {"model_name": model_name, "message": "Getting the LeNet model"}


# Define a route that calculates future age based on current age and a fixed number of years
# Notice how any parameter not defined in the path is treated as a query parameter

@app.get("/age/{age}", tags=["Note the query parameters with default values and optional parameters"])
async def calculate_age(age: int, years: int = 50, desired: int | None = None, activate: bool = True):
    future_age = age + years
    current_year = datetime.datetime.now().year
    future_year = current_year + years
    if desired is not None and activate:
        years_needed = desired - age
        if years_needed > 0:
            future_age = desired
            future_year = current_year + years_needed
    return {"current_age": age, "future_age": future_age, "year": future_year}
