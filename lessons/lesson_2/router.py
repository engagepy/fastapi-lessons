from enum import Enum

from fastapi import APIRouter

router = APIRouter(
    prefix="/lesson-2",
    tags=["Lesson 2"]
)

class ContactParameter(str, Enum):
    firstname = "firstname"
    lastname = "lastname"
    number = "number"
    email = "email"
    context = "context"
    gps = "gps"

class ContactGroup(str, Enum):
    personal = "personal"
    work = "work"
    business = "business"
    travel = "travel"

@router.get(
    "/greeting/{details}",
    summary="Multiple path parameters using Enum",
    description="Demonstrates the use of Enum for path parameters together with optional query parameters."
)
async def add_contact(
    details: ContactParameter,
    firstname: str,
    lastname: str,
    number: int,
    email: str,
    context: str | None = None,
    gps: str | None = None,
    group: ContactGroup = ContactGroup.personal
):
    contact_info = {
        "details": details,
        "firstname": firstname,
        "lastname": lastname,
        "number": number,
        "email": email,
        "context": context,
        "gps": gps,
        "group": group,
    }
    return {"contact_info": contact_info}