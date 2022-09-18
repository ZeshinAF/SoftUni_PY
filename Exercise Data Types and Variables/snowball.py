max = 0
max_w = 0
max_t = 0
max_q = 0
for i in range(0, int(input())):
    w = int(input())
    t = int(input())
    q = int(input())
    value = (w / t) ** q
    if int(value) > max:
        max = int(value)
        max_w = w
        max_t = t
        max_q = q
print(f"{max_w} : {max_t} = {max} ({max_q})")
