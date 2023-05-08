class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        return area

    def perimeter(self):
        perimeter = 4 * self.side
        return perimeter


class Rectangle:
    def __init__(self, length, b):
        self.length = length
        self.b = b

    def area(self):
        area = self.length * self.b
        return area

    def perimeter(self):
        perimeter = 2 * (self.b + self.length)
        return perimeter


shape = input().lower().strip()
obj_square = Square(4)
obj_rectangle = Rectangle(5, 6)
if shape == "square":
    print(f"Square area: {obj_square.area()}, perimeter : {obj_square.perimeter()}")
elif shape == "rectangle":
    print(f"rectangle area : {obj_rectangle.area()}, perimeter :{obj_rectangle.perimeter()}")
else:
    print("invalid")
