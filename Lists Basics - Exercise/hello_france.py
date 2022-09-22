items = [i.split('->') for i in input().split('|')]
budget = float(input())
resell = []

for i in items:
    type_of_item = i[0]
    price = float(i[1])
    if ((type_of_item == 'Clothes' and price <= 50) or (type_of_item == 'Shoes' and price <= 35) or (
            type_of_item == 'Accessories' and price <= 20.50)) and budget >= price:
        budget -= price
        resell.append(price*1.4)

budget += sum(resell)
profit = sum(resell) - sum(resell)/1.4

for i in resell:
    print(f'{i:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
