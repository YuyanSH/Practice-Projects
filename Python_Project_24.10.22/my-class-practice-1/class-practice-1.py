"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2
    
#from circle import Circle

circle_1 = Circle(42)
circle_2 = Circle(7)
#circle_1.radius = 100
print(circle_1.calculate_area())
"""

"""
#__value在外部其实是_SampleClass__value，即在内部变量名称前面加__会使该变量在外部的名称前面加上_类名称
class SampleClass:
    def __init__(self, value):
        self.__value = value
    def __method(self):
        print(self.__value)

sample_instance = SampleClass("hello")
sample_instance._SampleClass__method()
print(vars(sample_instance))
"""


