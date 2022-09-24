def min_of_three(x, y, z):
    r = x
    if y < x:
        r = y
    if z < r:
        r = z
    return r


i = int(input())
n = int(input())
m = int(input())
print(min_of_three(i, n, m))
