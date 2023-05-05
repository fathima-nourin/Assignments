class Calculator:
    def __init__(self, n1 , n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 *self.n2

    def division(self):
        return self.n1/self.n2


n1 = 10
n2 = 5

calculator = Calculator(n1, n2)

print(f"{n1} + {n2} = {calculator.add()}")

print(f"{n1} - {n2} = {calculator.subtract()}")
print(f"{n1} * {n2} = {calculator.multiplication()}")
print(f"{n1} / {n2} = {calculator.division()}")
