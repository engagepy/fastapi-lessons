from typing import Annotated
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum

router = APIRouter(
    prefix="/lesson-14",
    tags=["Lesson 14"]
)


class UserRole(BaseModel):
    name: str = Field(default="Angeline Jolie", example="admin", max_length=50)
    permissions: list[str] = Field(default=["read"], example=["read", "write", "delete"])


@router.post(
        "/user-role/{role_id}",
        summary="Body Parameters with Path Parameters",
        description="Demonstrates how to use Body() to accept a Pydantic model in the request body while also accepting path parameters for creating a user role",
        )
async def create_user_role(
    role_id: Annotated[int, Path(title="Role ID", description="The ID of the user role", gt=0)],
    user_role: Annotated[UserRole, Body(title="User Role", description="The details of the user role to create")]
):
    return {
        "role_id": role_id,
        "user_role": user_role.dict()
    }

