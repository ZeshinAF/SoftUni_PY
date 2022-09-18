budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
cost = flour_price + eggs_price + milk_price * 0.25
colored_eggs = 0
loaf_count = 0
counter = 0
while budget > cost:
    budget -= cost
    loaf_count += 1
    colored_eggs += 3
    counter += 1
    if counter == 3:
        colored_eggs -= loaf_count - 2
        counter = 0
print(f'You made {loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
