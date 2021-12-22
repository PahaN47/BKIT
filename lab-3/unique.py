class unique(object):
    def __init__(self, *items, ignore_case=False):
        all_items = []
        for item in items:
            if type(item) is not list:
                all_items.append(item)
                continue
            all_items += item
        
        self.items = []
        for item in all_items:
            if type(item) is str and ignore_case:
                if item.lower() not in list(map(str.lower, self.items)):
                    self.items.append(item)
                continue
            if item not in self.items:
                self.items.append(item)
        self.pos = -1

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.items):
            raise StopIteration
        return self.items[self.pos]

    def __iter__(self):
        return self

if __name__ == '__main__':
    for item in unique(1, 2, [1, 2, 3, 4], 7, 0, ignore_case=False):
        print(item)
            