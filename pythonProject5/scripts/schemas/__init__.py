from typing import List

from pydantic import BaseModel


class Inventory(BaseModel):
    id: int
    item_name: str
    quantity: int
    cost: int
    update: bool
    count: int = 0


class ResponseModel(BaseModel):
    id: int
    item_name: str
    quantity: int
    cost: int


class Email(BaseModel):
    email: str
