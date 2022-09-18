n = int(input())
for i in range(0, n):
    s = input()
    if ',' in s or '.' in s or '_' in s:
        print(f'{s} is not pure!')
    else:
        print(f'{s} is pure.')
