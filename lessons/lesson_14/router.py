from typing import Annotated
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum

router = APIRouter(
    prefix="/lesson-14",
    tags=["Lesson 14"]
)

