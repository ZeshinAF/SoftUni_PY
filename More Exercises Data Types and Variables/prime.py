n = int(input())
prime = True
for i in range(n-1, 1, -1):
    if n % i == 0:
        prime = False
print(prime)
