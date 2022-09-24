def sum_numbers(x, y):
    return x + y


def subtract(x, y):
    return x - y


def add_and_subtract(x, y, z):
    g = sum_numbers(x, y)
    return subtract(g, z)


x = int(input())
y = int(input())
z = int(input())
print(add_and_subtract(x, y, z))
