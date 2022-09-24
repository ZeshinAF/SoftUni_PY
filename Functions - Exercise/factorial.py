def factorial_division(x, y):
    fac_x = 1
    for i in range(1, x + 1):
        fac_x *= i
    fac_y = 1
    for i in range(1, y + 1):
        fac_y *= int(i)
    print(f'{fac_x / fac_y:.2f}')


n = int(input())
m = int(input())
factorial_division(n, m)
