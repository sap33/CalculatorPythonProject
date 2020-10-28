def addition(a, b):
    return a + b

def subtraction(a, b):
    return b - a

def multiplication(a, b):
    return b * a

def division(a, b):
    return round(b / a, 9)

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

    def mul(self, x, y):
        x = int(x)
        y = int(y)
        self.result = multiplication(x, y)
        return self.result

    def div(self, x, y):
        x = float(x)
        y = float(y)
        self.result = division(x, y)
        return self.result