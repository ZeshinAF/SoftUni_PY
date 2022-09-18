n = int(input())
for i in range(1, n + 1):
    sum = 0
    digit = i
    while digit > 0:
        sum += digit % 10
        digit //= 10
    print(f'{i} -> {sum == 5 or sum == 7 or sum == 11}')
