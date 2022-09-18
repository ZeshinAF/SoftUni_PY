n = input().lower()
c = 0
while 'sand' in n:
    c += 1
    n = n.replace('sand', '', 1)
while 'water' in n:
    c += 1
    n = n.replace('water', '', 1)
while 'fish' in n:
    c += 1
    n = n.replace('fish', '', 1)
while 'sun' in n:
    c += 1
    n = n.replace('sun', '', 1)
print(c)