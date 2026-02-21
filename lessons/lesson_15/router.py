from typing import Annotated
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel, Field
import enum


router = APIRouter(
    prefix="/lesson-15",
    tags=["Lesson 15"]
)


