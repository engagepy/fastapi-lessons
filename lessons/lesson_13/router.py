from fastapi import APIRouter, Path, Query
import enum
from pydantic import BaseModel, Field
from typing import Annotated, Literal 


router = APIRouter(
    prefix="/lesson-13",
    tags=["Lesson 13"]
)

