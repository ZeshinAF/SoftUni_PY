from sys import maxsize

nums = [int(i) for i in input().split(' ')]
while True:
    c = input().split(' ')
    if c[0] == 'end':
        print(nums)
        break
    if c[0] == 'exchange':
        new = []
        index = int(c[1])
        if index > len(nums) - 1 or index < 0:
            print('Invalid index')
        else:
            for i in range(0, index + 1):
                new.append(nums[i])
            for i in new:
                nums.remove(i)
            nums += new
    if c[0] == 'max':
        index = 'No matches'
        max = -maxsize
        if c[1] == 'even':
            for i in range(0, len(nums)):
                if nums[i] % 2 == 0 and nums[i] >= max:
                    max = nums[i]
                    index = i
        elif c[1] == 'odd':
            for i in range(0, len(nums)):
                if nums[i] % 2 != 0 and nums[i] >= max:
                    max = nums[i]
                    index = i
        print(index)
    if c[0] == 'min':
        index = 'No matches'
        min = +maxsize
        if c[1] == 'even':
            for i in range(0, len(nums)):
                if nums[i] % 2 == 0 and nums[i] <= min:
                    min = nums[i]
                    index = i
        elif c[1] == 'odd':
            for i in range(0, len(nums)):
                if nums[i] % 2 != 0 and nums[i] <= min:
                    min = nums[i]
                    index = i
        print(index)
    if c[0] == 'first':

        count = int(c[1])
        if count > len(nums):
            print('Invalid count')
        elif c[2] == 'even':
            f = []
            a = 0
            while a < len(nums):
                if nums[a] % 2 == 0:
                    f.append(nums[a])
                if len(f) == count:
                    break
                a += 1
            print(f)
        elif c[2] == 'odd':
            f = []
            a = 0
            while a < len(nums):
                if nums[a] % 2 != 0:
                    f.append(nums[a])
                if len(f) == count:
                    break
                a += 1
            print(f)
    if c[0] == 'last':
        count = int(c[1])
        if count > len(nums):
            print('Invalid count')
        elif c[2] == 'even':
            f = []
            a = 0
            while a < len(nums):
                if nums[a] % 2 == 0:
                    f.append(nums[a])
                a += 1
            if len(f) > count:
                for i in range(0, len(f) - count):
                    f.pop(i)
            print(f)
        elif c[2] == 'odd':
            f = []
            a = 0
            while a < len(nums):
                if nums[a] % 2 != 0:
                    f.append(nums[a])
                a += 1
            if len(f) > count:
                for i in range(0, len(f) - count):
                    f.pop(i)
            print(f)
