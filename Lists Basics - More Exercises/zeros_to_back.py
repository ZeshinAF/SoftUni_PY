# nums = [int(i) for i in input().split(", ")]
# zeros = []
# while 0 in nums:
#     zeros.append(0)
#     nums.remove(0)
# nums += zeros
# print(nums)

nums = input().split(', ')
final = []
for i in nums:
    if i != '0':
        final.append(int(i))
for i in nums:
    if i == '0':
        final.append(int(i))
print(final)
