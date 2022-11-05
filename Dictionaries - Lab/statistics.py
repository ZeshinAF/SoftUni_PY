products = {}
while True:
    x = input()
    if x == 'statistics':
        break
    else:
        key, value = x.split(': ')
        if key in products:
            products[key] += int(value)
        else:
            products[key] = int(value)
print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
