line = input().split(' ')
dic = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    dic[key] = value
search = input().split(' ')
for i in search:
    if i in dic.keys():
        print(f"We have {dic[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
