import enum
import random
from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import AfterValidator

router = APIRouter(
    prefix="/lesson-9",
    tags=["Lesson 9"]
)

services = {
    "wifi": "Available",
    "sim": "24/7 Support",
    "robot": "Fast Delivery",
    "smart_home": "Automated Services"
}

def check_service(value: str):
    if value is None:
        return value
    for service in value:
        if service not in services:
            raise ValueError(f"Service `{service}` is not valid. Choose from: {', '.join(services)}")
    return value

class CountryEnum(str, enum.Enum):
   IN = "IN"
   USA = "USA"
   UK = "UK"
   AUS = "AUS"
   CAN = "CAN"


@router.put(
    "/isp/{country}",
    summary="Path parameter validation and metadata using AfterValidator and Enum",
    description="Demonstrates path parameter validation using AfterValidator and Enum from Pydantic."
)
async def country_service(
    country: CountryEnum,
    q : Annotated[list[str] | None, Query( title="Services required", alias="service-list"), AfterValidator(check_service)] = None
):
    results = {
        "service_info": [
            {"country_code": country},
            {"service_availability": "Available"}, 
            {"next_activation": random.choice(list(CountryEnum))}
            ]}
    results.update()
    if q:
        results.update({"services_requested": q})
    return results

