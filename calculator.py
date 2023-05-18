operation = input("enter the type of operation")


class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number2 * self.number2

    def division(self):
        return self.number1 / self.number2


calc = Calculator(10, 5)
if operation == "+":
    print(calc.addition())
elif operation == "-":
    print(calc.subtraction())
elif operation == "*":
    print(calc.multiplication())
elif operation == "/":
    print(calc.division())
else:
    print("0")
