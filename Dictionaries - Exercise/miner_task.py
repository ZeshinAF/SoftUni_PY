resources = {}
while True:
    metal = input()
    if metal == 'stop':
        break
    quantity = int(input())
    if metal in resources:
        resources[metal] += quantity
    else:
        resources[metal] = quantity
for k, v in resources.items():
    print(f"{k} -> {v}")
