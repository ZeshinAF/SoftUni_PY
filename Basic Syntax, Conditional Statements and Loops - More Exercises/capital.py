n = input()
l = []
for i,v in enumerate(n):
    if str.isupper(v):
        l.append(i)
print(l)