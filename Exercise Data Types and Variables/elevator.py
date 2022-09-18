people = int(input())
capacity = int(input())
c = 0
while people > 0:
    cour = people // capacity
    if cour == 0:
        c += 1
    else:
        c += cour
    people -= capacity * c
print(c)
