from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/lesson-3",
    tags=["Lesson 3"]
)

class ContactGroup(str, Enum):
    personal = "personal"
    work = "work"
    business = "business"
    travel = "travel"

class ContactParameter(BaseModel):
    first_name: str
    last_name: str
    number: int
    email: str
    context: str | None = None
    gps: float | None = None
    group: ContactGroup = ContactGroup.personal

@router.post(
    "/contact/",
    summary="Request body with Pydantic model and Enum",
    description="Demonstrates a request body using a Pydantic model and an Enum for controlled values."
)
async def add_contact(
    details: ContactParameter,
    group: ContactGroup = ContactGroup.personal
):
    contact_info = {
        "firstname": details.first_name.casefold(),
        "lastname": details.last_name.casefold(),
        "number": details.number,
        "email": details.email.casefold(),
        "context": details.context.casefold() if details.context else None,
        "gps": details.gps,
        "group": group,
    }
    return {"contact_info": contact_info}