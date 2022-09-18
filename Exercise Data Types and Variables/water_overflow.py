cap = 0
for i in range(0, int(input())):
    n = int(input())
    if cap + n <= 255:
        cap += n
    else:
        print("Insufficient capacity!")
print(cap)
