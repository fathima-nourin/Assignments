from pydantic import BaseModel


class Inventory(BaseModel):
    id: int
    item_name: str
    quantity: int
    cost: int
