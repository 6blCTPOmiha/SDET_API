from pydantic import BaseModel
from typing import Dict, List, Any
from models.addition_model import AdditionModelResponse, AdditionModelRequest


class EntityModelRequest(BaseModel):
    title: str
    verified: bool
    addition: AdditionModelRequest
    important_numbers: List[int]


class EntityModelResponse(BaseModel):
    id: int
    title: str
    verified: bool
    addition: AdditionModelResponse
    important_numbers: List[int]
