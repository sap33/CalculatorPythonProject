def addition(a, b):
    return a + b

def subtraction(a, b):
    return b - a

def multiplication(a, b):
    return b * a

def division(a, b):
    return round(b / a, 9)

def square(a):
    return a * a

def squareroot(a):
     return a ** (1 / 2)

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

    def squ(self, x):
        x = int(x)
        self.result = square(x)
        return self.result

    def squareroot(self, x):
        x = float(x)
        self.result = float('{:.10}'.format(squareroot(x)))
        return self.result

