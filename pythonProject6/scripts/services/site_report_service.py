from fastapi import APIRouter

from scripts.constants.app_constants import EndPoints
from scripts.core.handlers.calculate import Calculator
from scripts.schemas import CalculationInput

router = APIRouter(prefix=EndPoints.api_calculate)
calculator = Calculator()


#
# @router.post(EndPoints.api_calculate)
# def perform_calculation(req_json: CalculationInput):
#     try:
#         return {"calculate": "true"}
#
#     except Exception as e:
#         print(e)


@router.post("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    try:
        result = calculator.add(num1, num2)
    except TypeError:
        return {"error": "Invalid input types. Please provide integers."}
    return {"result": result}


@router.post("/subtract")
async def subtract(inputs: CalculationInput):
    try:
        result = calculator.subtract(inputs.num1, inputs.num2)
    except TypeError:
        return {"error": "Invalid input types. Please provide integers."}
    return {"result": result}


@router.post("/multiply")
async def multiply(num1: int, num2: int):
    try:
        result = calculator.multiply(num1, num2)
    except TypeError:
        return {"error": "Invalid input types. Please provide integers."}
    return {"result": result}


@router.post("/divide/{num1}/{numb2}")
async def divide(num1: int, num2: int):
    try:
        result = calculator.divide(num1, num2)
    except ZeroDivisionError as e:
        return {"error": str(e)}
    except TypeError:
        return {"error": "Invalid input types. Please provide integers."}
    return {"result": result}
