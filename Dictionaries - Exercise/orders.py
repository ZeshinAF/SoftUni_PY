products = {}
while True:
    product = input()
    if product == 'buy':
        break
    name, price, quantity = product.split(' ')
    if name not in products:
        products[name] = [0.0, 0]
    products[name][0] = float(price)
    products[name][1] += int(quantity)
for k, v in products.items():
    print(f"{k} -> {v[0] * v[1]:.2f}")
