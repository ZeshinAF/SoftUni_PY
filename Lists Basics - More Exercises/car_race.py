# sequence = [int(i) for i in input().split(' ')]
sequence = input().split(' ')
left = 0
right = 0
for i in range(0, len(sequence) // 2):
    if sequence[i] != '0':
        left += int(sequence[i])
    else:
        left *= 0.8
for i in range(len(sequence) - 1, len(sequence) // 2, -1):
    if sequence[i] != '0':
        right += int(sequence[i])
    else:
        right *= 0.8
if left > right:
    print(f"The winner is right with total time: {right:.1f}")
else:
    print(f"The winner is left with total time: {left:.1f}")
