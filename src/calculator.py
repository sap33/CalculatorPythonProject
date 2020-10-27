def addition(a, b):
    return a + b

class calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        x = int(x)
        y = int(y)
        self.result = addition(x, y)
        return self.result


