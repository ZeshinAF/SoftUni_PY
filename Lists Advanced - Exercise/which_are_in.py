subs = input().split(', ')
strings = input().split(', ')
are_in = []
for i in subs:
    for j in strings:
        if i in j and i not in are_in:
            are_in.append(i)
print(are_in)
