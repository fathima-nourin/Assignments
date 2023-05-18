from pydantic import BaseModel


class CalculationInput(BaseModel):
    num1: int
    num2: int
