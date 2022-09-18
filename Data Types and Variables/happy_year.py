n = int(input())
while len(set(str(n))) != len(str(n)):
    n+=1
print(n)