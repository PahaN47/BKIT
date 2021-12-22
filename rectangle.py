from lab_python_oop.geometric_base import geometric_base as gb

class rectangle(gb):

    name = "Прямоугольник"


    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

    def area(self):
        return self.height * self.width

    def repr(self):
        return "Длина: {}\nШирина: {}\nЦвет: {}".format(self.height, self.width, self.color)

