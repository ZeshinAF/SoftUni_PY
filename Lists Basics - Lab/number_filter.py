nums = []
for _ in range(int(input())):
    nums.append(int(input()))
command = input()
if command == 'even':
    for i in range(len(nums) - 1, -1, -1):
        element = nums[i]
        if not element % 2 == 0:
            nums.remove(element)
elif command == 'odd':
    for i in range(len(nums) - 1, -1, -1):
        element = nums[i]
        if element % 2 == 0:
            nums.remove(element)
elif command == 'positive':
    for i in range(len(nums) - 1, -1, -1):
        element = nums[i]
        if not element >= 0:
            nums.remove(element)
elif command == 'negative':
    for i in range(len(nums) - 1, -1, -1):
        element = nums[i]
        if element >= 0:
            nums.remove(element)
print(nums)