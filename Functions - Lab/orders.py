def order_price(item, quantity):
    if item == 'coffee':
        return quantity * 1.5
    elif item == 'water':
        return quantity * 1.0
    elif item == 'coke':
        return quantity * 1.4
    elif item == 'snacks':
        return quantity * 2.0


n = input()
m = int(input())
print(f'{order_price(item=n, quantity=m):.2f}')
