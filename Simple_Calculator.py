def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


def simpleinterest(p, r, t):
    return (p * r * t) / 100


def compoundinterest(P, R, T):
    return P * pow((1 + r / 100), T)


def squareroot(num):
    return num**0.5


print(simpleinterest(5000, 10, 6))
