q = input().split(', ')
if q[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    print(f'Oi! Sheep number {len(q)-q.index("wolf")-1}! You are about to be eaten by a wolf!')
