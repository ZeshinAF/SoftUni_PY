def abs_list(n):
    new_list = []
    for i in n:
        new_list.append(abs(float(i)))
    return new_list


nums = abs_list(input().split(' '))
print(nums)
