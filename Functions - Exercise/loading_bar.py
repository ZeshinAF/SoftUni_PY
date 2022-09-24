def loading_bar(x):
    bar = list('[..........]')
    for i in range(1, x//10+1):
        bar[i] = '%'
    return ''.join(bar)


n = int(input())
if n == 100:
    print("100% Complete!")
    print(f"{loading_bar(n)}")
else:
    print(f"{n}% {loading_bar(n)}")
    print("Still loading...")



