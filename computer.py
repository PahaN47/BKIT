class computer:
    id = 0

    def __init__(self, name):
        self.__id = computer.id
        computer.id += 1
        self.name = name

    def getid(self):
        return self.__id