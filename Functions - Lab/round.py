def round_list(nums):
    for i in range(0, len(nums)):
        nums[i] = round(nums[i])


nums = [float(i) for i in input().split(' ')]
round_list(nums)
print(nums)
