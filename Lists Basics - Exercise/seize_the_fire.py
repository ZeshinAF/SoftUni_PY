cells = [i.split('=') for i in input().replace(' ', '').split('#')]
water = int(input())
fire = 0
effort = 0
put_out = []
for i in cells:
    type_of_fire = i[0]
    value_of_cell = int(i[1])
    if ((type_of_fire == 'High' and 81 <= value_of_cell <= 125) or (
            type_of_fire == 'Medium' and 51 <= value_of_cell <= 80) or (
            type_of_fire == 'Low' and 1 <= value_of_cell <= 50)) and water >= value_of_cell:
        fire += value_of_cell
        water -= value_of_cell
        effort += value_of_cell * 0.25
        put_out.append(value_of_cell)
print('Cells:')
for i in put_out:
    print(f'- {i}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire}')
