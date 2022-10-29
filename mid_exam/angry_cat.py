def right_items(items, entry_point, type):
    sum = 0
    if type == 'cheap':
        for i in range(entry_point+1, len(items)):
            item = items[i]
            if item < items[entry_point]:
                sum += item
    elif type == 'expensive':
        for i in range(entry_point+1, len(items)):
            item = items[i]
            if item >= items[entry_point]:
                sum += item
    return sum

def left_items(items, entry_point, type):
    sum = 0
    if type == 'cheap':
        for i in range(entry_point):
            item = items[i]
            if item < items[entry_point]:
                sum += item
    elif type == 'expensive':
        for i in range(entry_point):
            item = items[i]
            if item >= items[entry_point]:
                sum += item
    return sum


prices = [int(x) for x in input().split(', ')]
entry_point = int(input())  # index
type_of_items = input()
left = left_items(prices, entry_point, type_of_items)
right = right_items(prices, entry_point, type_of_items)
if left >= right:
    print(f'Left - {left}')
else:
    print(f'Right - {right}')
