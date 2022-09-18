decoration_quantity = int(input())
days_left = int(input())
budget = 0
points = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        decoration_quantity += 2
    if i % 2 == 0:
        points += 5
        budget += decoration_quantity * 2
    if i % 3 == 0:
        points += 3 + 10
        budget += decoration_quantity * 8
    if i % 5 == 0:
        points += 17
        budget += decoration_quantity * 15
    if i % 5 == 0 and i % 3 == 0:
        points += 30
    if i % 10 == 0:
        points -= 20
        budget += 23
        if i == days_left:
            points -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {points}")
