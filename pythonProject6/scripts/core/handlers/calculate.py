

class Calculator:
    @staticmethod
    def add(num1: int, num2: int):
      #  {"status": "success/failed","message":"fetch data success","data":{}}
        return num1 + num2

    @staticmethod
    def subtract(num1: int, num2: int):
        return num1 - num2

    @staticmethod
    def multiply(num1: int, num2: int):
        return num1 * num2

    @staticmethod
    def divide(num1: int, num2: int):
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2


