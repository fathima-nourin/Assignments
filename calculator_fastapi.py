from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{number1}/{number2}")
async def add(number1: int, number2: int):
    return {"result": number1 + number2}


@app.get("/subtract/{number1}/{number2}")
async def subtract(number1: int, number2: int):
    return {"result": number1 - number2}


@app.get("/multiply/{number1}/{number2}")
async def multiply(number1: int, number2: int):
    return {"result": number1 * number2}


@app.get("/divide/{number1}/{number2}")
async def divide(number1: int, number2: int):
    if number2 == 0:
        print("error")
    else:
        return {"result": number1 / number2}
