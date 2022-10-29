coffees = input().split(' ')
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split(' ')
    if command[0] == 'Include':
        coffees.append(command[1])
    elif command[0] == 'Remove':
        numbers_of_coffees = int(command[2])
        if command[1] == 'first':
            for _ in range(numbers_of_coffees):
                coffees.pop(0)
        elif command[1] == 'last':
            for _ in range(numbers_of_coffees):
                coffees.pop()
    elif command[0] == 'Prefer':
        first_index, second_index = int(command[1]), int(command[2])
        if first_index < len(coffees) and second_index < len(coffees):
            coffees[first_index], coffees[second_index] = coffees[second_index], coffees[first_index]
    elif command[0] == 'Reverse':
        coffees.reverse()
print("Coffees:")
[print(x, end=' ') for x in coffees]
