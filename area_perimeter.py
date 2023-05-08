class Square:
    def __init__(self, side):
        """this is the construct to initialize the side of the square"""
        self.side = side

    def area(self):
        """this is the function to calculate the area of the square"""
        area = self.side * self.side
        return area

    def perimeter(self):
        """this is the function to calculate the perimeter of the square"""
        perimeter = 4 * self.side
        return perimeter


class Rectangle:
    def __init__(self, length, width):
        """ This is the constructor to initialize the length and breadth"""
        self.length = length
        self.width = width

    def area(self):
        """this is the function to calculate the area of rectangle"""
        area = self.length * self.width
        return area

    def perimeter(self):
        """this is to calculate the perimeter of the rectangle"""
        perimeter = 2 * (self.width + self.length)
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
