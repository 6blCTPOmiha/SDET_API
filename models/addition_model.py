from pydantic import BaseModel


class AdditionModelRequest(BaseModel):
    additional_info: str
    additional_number: int


class AdditionModelResponse(BaseModel):
    id: int
    additional_info: str
    additional_number: int
