def chars_in_range(x, y):
    for i in range(ord(x) + 1, ord(y)):
        print(chr(i), end=' ')


n = input()
m = input()
chars_in_range(n, m)
