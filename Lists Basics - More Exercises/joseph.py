nums = input().split(' ')
n = int(input())
final = []

idx = (n - 1) % len(nums)
while len(nums) > 1:
    final.append(nums[idx])
    nums.pop(idx)
    idx = (n - 1 + idx) % len(nums)
final.append(nums[0])

print('[' + final[0], end='')
for i in range(1, len(final)):
    print(',' + final[i], end='')
print(']')
