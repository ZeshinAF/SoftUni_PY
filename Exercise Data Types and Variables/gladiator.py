losses = int(input())
h = float(input())
s = float(input())
sh = float(input())
a = float(input())
expenses = 0
counter = 1
for i in range(1, losses+1):
    if i % 2 == 0:
        expenses += h
    if i % 3 == 0:
        expenses += s
        if i % 2 == 0:
            if counter % 2 == 0:
                expenses += sh + a
                counter += 1
            else:
                expenses += sh
                counter += 1

print(f"Gladiator expenses: {expenses:.2f} aureus")
