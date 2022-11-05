line = input().split(' ')
dic = {}
for i in range(0, len(line), 2):
    key = line[i]
    value = int(line[i + 1])
    dic[key] = value
print(dic)