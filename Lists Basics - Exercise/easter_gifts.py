gifts = input().split(' ')
command = input()
while command != "No Money":
    command = command.split(' ')
    gift = command[1]
    if not gift:
        continue
    if command[0] == 'OutOfStock':
        for i in range(0, len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command[0] == 'JustInCase':
        gifts[-1] = gift
    command = input()
for i in gifts:
    if i != 'None':
        print(i, end=' ')