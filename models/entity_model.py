from pydantic import BaseModel
from typing import Dict, List, Any


class EntityModelRequest(BaseModel):
    addition: Dict[str, int]
    important_numbers: List[int]
    title: str
    verified: bool


class EntityModelResponse(BaseModel):
    id: int
    addition: Dict[str, Any]
    important_numbers: List[int]
    title: str
    verified: bool
