a = 11
b = 11
a_card = []
b_card = []
sequence = input().split(' ')
for i in sequence:
    team = i[0]
    num = int(i[1:])
    if team == 'A' and num not in a_card:
        a -= 1
        a_card.append(num)
    if team == 'B' and num not in b_card:
        b -= 1
        b_card.append(num)
    if a < 7 or b < 7:
        print(f"Team A - {a}; Team B - {b}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {a}; Team B - {b}")
