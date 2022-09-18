divisor = int(input())
bound = int(input())
lar = 1
for i in range(lar, bound+1):
    if i*divisor > bound:
        break
    lar = i*divisor
print(lar)