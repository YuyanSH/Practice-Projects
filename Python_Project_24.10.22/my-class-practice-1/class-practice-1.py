import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
from circle import Circle

circle_1 = Circle(42)
circle_2 = Circle(7)

circle_1

circle_2

print(circle_1.calculate_area())
