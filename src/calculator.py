def addition(a, b):
    return a + b

def subtraction(a, b):
    return b - a


class calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        x = int(x)
        y = int(y)
        self.result = addition(x, y)
        return self.result

    def sub(self, x, y):
        x = int(x)
        y = int(y)
        self.result = subtraction(x, y)
        return self.result
