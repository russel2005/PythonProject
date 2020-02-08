print('calculator module')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divided(x, y):
    if y == 0:
        raise ValueError('can\'t divided by zero!')
    return x / y


