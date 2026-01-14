from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


app = FastAPI(title="Lesson 3 - Request Body Parameters with Pydantic", version="1.0.0", description="An example FastAPI application demonstrating request body parameters using Pydantic models along with Enums for specific fields.")

# To run the application, use the command: `uvicorn main:app --reload`

#Define an enumeration for model names to restrict valid input values in path parameters

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


#Define an enumeration for contact groups to restrict valid input values in path parameters


#Route that demonstrates form fields instead of a single body parameter
@app.post("/greeting/", tags=["Observe request body parameters using Pydantic Model & Enum"])
async def add_contact(details: ContactParameter, group: ContactGroup = ContactGroup.personal):
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

