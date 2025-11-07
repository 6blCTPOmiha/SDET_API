from pydantic import BaseModel


class EntityModelRequest(BaseModel):
    addition: dict[str, int]
    important_numbers: dict[int]
    title: str
    verified: bool


class EntityModelResponse(BaseModel):
    addition: dict[str, int, int]
    id: int
    important_numbers = dict[int]
    title: str
    verified: bool
