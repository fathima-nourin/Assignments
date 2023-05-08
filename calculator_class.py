class Calculator:
    def __init__(self, first, second):
        """this is a constructor to initialize the numbers for operation"""
        self.first = first
        self.second = second

    def add(self):
        """this is the function to add the given numbers"""
        return self.first + self.second

    def subtract(self):
        """this is the function to subtract the given numbers"""
        return self.first - self.second

    def multiplication(self):
        """this is the function to multiply two numbers"""
        return self.first * self.second

    def division(self):
        """this is the function to divide the given numbers"""
        return self.first / self.second


first = 10
second = 5

calculator = Calculator(first, second)

print(f"{first} + {second} = {calculator.add()}")

print(f"{first} - {second} = {calculator.subtract()}")
print(f"{first} * {second} = {calculator.multiplication()}")
print(f"{first} / {second} = {calculator.division()}")
