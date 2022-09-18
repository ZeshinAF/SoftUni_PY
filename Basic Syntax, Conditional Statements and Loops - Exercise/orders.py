n = int(input())
total = 0
for i in range(0, n):
    ppc = float(input())
    days = int(input())
    cpd = int(input())
    if 0.01 <= ppc <= 100.00 and 1 <= days <= 31 and 1 <= cpd <= 2000:
        total += ppc * days * cpd
        print(f'The price for the coffee is: ${ppc * days * cpd:.2f}')
print(f'Total: ${total:.2f}')
