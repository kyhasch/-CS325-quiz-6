from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

# Additional shapes can be added without modifying existing code
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

if __name__ == "__main__":
    shapes = [Circle(5), Square(4), Rectangle(3, 6), Triangle(4, 5)]
    
    for shape in shapes:
        print("Area of", type(shape).__name__, ":", shape.get_area())