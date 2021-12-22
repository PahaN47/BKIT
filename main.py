from lab_python_oop.rectangle import rectangle
from lab_python_oop.circle import circle
from lab_python_oop.square import square
import numpy as np


if __name__ == "__main__":
    r = rectangle(8, 8, "синий")
    print(r.area())
    print(r.repr())
    c = circle(8, "зеленый")
    print(c.area())
    print(c.repr())
    s = square(8, "красный")
    print(s.area())
    print(s.repr())
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    arr.shape = (2, 3)
    print(arr)
