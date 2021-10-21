class microprocessor:
    id = 0

    def __init__(self, name, price, comp_id):
        self.__id = microprocessor.id
        microprocessor.id += 1
        self.name = name
        self.price = price
        self.comp_id = comp_id

    def getid(self):
        return self.__id