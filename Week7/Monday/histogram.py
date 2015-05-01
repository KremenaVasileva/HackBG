class Histogram:
    def __init__(self):
        self.h_dict = {}

    def add(self, item):
        if item not in self.h_dict:
            self.h_dict[item] = 1
        else:
            self.h_dict[item] += 1

    def count(self, item):
        if item not in self.h_dict:
            return None
        else:
            return self.h_dict[item]

    def get_dict(self):
        return self.h_dict

    def items(self):
        pass
