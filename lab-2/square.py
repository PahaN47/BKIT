from lab_python_oop.rectangle import rectangle

class square(rectangle):

    name = "Квадрат"

    def __init__(self, size, color):
        self.size = size
        super().__init__(size, size, color)

    def repr(self):
        return "Длина стороны: {}\nЦвет: {}".format(self.size, self.color)
        