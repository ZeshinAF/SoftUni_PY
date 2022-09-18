n = int(input())
balanced = True
for i in range(0, n):
    a = input()
    if a == ')' and balanced is True:
        balanced = False
        break
    elif a == ')':
        balanced = True
    elif a == '(' and balanced is False:
        break
    elif a == '(':
        balanced = False
if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')