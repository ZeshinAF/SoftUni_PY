def add_update(list, num=2):
    if list[num] < 9:
        list[num] += 1
        return list
    else:
        list[num] = 0
        add_update(list, num-1)


version = [int(i) for i in input().split('.')]
add_update(version)
print(f'{version[0]}.{version[1]}.{version[2]}')


