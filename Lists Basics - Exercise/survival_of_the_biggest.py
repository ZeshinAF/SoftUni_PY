nums = input().split(' ')
for i, v in enumerate(nums):
    nums[i] = int(v)
n = int(input())
for _ in range(0, n):
    nums.remove(min(nums))
print(str(nums).replace("[", "").replace("]", ""))
