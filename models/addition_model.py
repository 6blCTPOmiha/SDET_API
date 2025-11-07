from pydantic import BaseModel


class AdditionModelRequest(BaseModel):
    additional_info: str
    additional_number: int


class AdditionModelResponse(BaseModel):
    additional_info: str
    additional_number: int
    id: int
