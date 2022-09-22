nums = input().split(', ')
beggars_count = int(input())
beggars = []
for _ in range(beggars_count):
    beggars.append(0)
for i in range(0, len(nums)):
    beggars[i%beggars_count] += int(nums[i])
print(beggars)
