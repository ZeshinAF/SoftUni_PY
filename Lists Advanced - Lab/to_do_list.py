notes = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    items = command.split('-')
    priority = int(items[0])-1
    note = items[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [i for i in notes if i != 0]
print(result)
