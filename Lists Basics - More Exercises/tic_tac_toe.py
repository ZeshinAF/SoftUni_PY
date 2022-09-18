f = input().split(' ')  # first
s = input().split(' ')  # second
t = input().split(' ')  # third
b = [f, s, t]  # board
for i in range(0, len(f)):
    if (b[0][0] == b[1][1] == b[2][2]) or (b[0][2] == b[1][1] == b[2][0]):
        if b[1][1] == '1':
            print("First player won")
            break
        elif b[1][1] == '2':
            print("Second player won")
            break
    col = ''
    for j in range(0, len(f)):
        col += (b[j][i])
    if col == '111':
        print("First player won")
        break
    elif col == '222':
        print("Second player won")
        break
    row = ''.join(b[i])
    if row == '111':
        print("First player won")
        break
    elif row == '222':
        print("Second player won")
        break
else:
    print("Draw!")
