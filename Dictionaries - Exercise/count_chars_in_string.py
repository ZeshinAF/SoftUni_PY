words = input().split(' ')
occ = {}
for i in words:
    for j in i:
        if j in occ:
            occ[j] += 1
        else:
            occ[j] = 1
for k, v in occ.items():
    print(f"{k} -> {v}")
