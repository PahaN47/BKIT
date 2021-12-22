from lab_python_oop.geometric_base import geometric_base as gb
from math import pi, radians

class circle(gb):

    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        return pi * self.radius * self.radius
    
    def repr(self):
        return "Радиус: {}\nЦвет: {}".format(self.radius, self.color)
        