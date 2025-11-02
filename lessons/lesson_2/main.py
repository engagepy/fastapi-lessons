from enum import Enum
from fastapi import FastAPI
import datetime

app = FastAPI(title="Lesson 2 - Multiple Path Parameters", version="1.0.0", description="An example FastAPI application demonstrating contact management with multiple path parameters. Also worth noting the use of Enums for path parameters as well as optional query parameters.")

# To run the application, use the command: `uvicorn main:app --reload`

#Define an enumeration for model names to restrict valid input values in path parameters
class ContactParameter(str, Enum):
    first_name = "first_name"
    last_name = "last_name"
    number = "number"
    email = "email"
    context = "context"
    gps = "gps"


#Define an enumeration for contact groups to restrict valid input values in path parameters
class ContactGroup(str, Enum):
    personal = "personal"
    work = "work"
    business = "business"
    travel = "travel"


#Route that demonstrates multiple path parameters using Enum
@app.get("/greeting/{details: ContactParameter}", tags=["Observe multiple path & query parameters using Enum"])
async def add_contact(
    name: str,
    lastname: str,
    number: int,
    email: str,
    context: str | None = None,
    gps: float | None = None,
    group: ContactGroup = ContactGroup.personal
):
    contact_info = {
        "name": name,
        "lastname": lastname,
        "number": number,
        "email": email,
        "context": context,
        "gps": gps,
        "group": group,
    }
    return {"contact_info": contact_info}
