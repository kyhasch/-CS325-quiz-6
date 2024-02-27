import math

class Shape:
    def get_area(self):
        pass

    def set_width(self, width):
        pass

    def set_height(self, height):
        pass

    def set_base(self, base):
        pass

    def set_side(self, side):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def set_width(self, width):
        self.radius = width / 2

    def set_height(self, height):
        self.radius = height / 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def set_base(self, base):
        self.base = base

    def set_height(self, height):
        self.height = height

class Polygon(Shape):
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def get_area(self):
        return (self.sides * self.length ** 2) / (4 * math.tan(math.pi / self.sides))

    def set_side(self, side):
        self.length = side

# Example usage
if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(3, 6), Triangle(4, 5), Polygon(6, 4)]
    for shape in shapes:
        print("Area of", type(shape).__name__, ":", shape.get_area())
