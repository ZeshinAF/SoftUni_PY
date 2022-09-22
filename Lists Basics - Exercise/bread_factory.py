events = [i.split('-') for i in input().split('|')]
energy = 100
coins = 100
for i in events:
    number = int(i[1])
    if i[0] == 'rest':
        if energy + number > 100:
            print(f'You gained {100 - energy} energy.')
            energy = 100
        else:
            energy += number
            print(f'You gained {number} energy.')
        print(f"Current energy: {energy}.")
    elif i[0] == 'order':
        if energy - 30 >= 0:
            print(f"You earned {number} coins.")
            coins += number
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        if coins - number >= 0:
            print(f"You bought {i[0]}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {i[0]}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")