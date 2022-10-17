def group_numbers(numbers, boundary=10):
    if len(numbers) != 0:
        group = []
        for i in numbers:
            if i <= boundary:
                group.append(i)
        for i in group:
            numbers.remove(i)
        print(f"Group of {boundary}'s: {group}")
        group_numbers(numbers, boundary+10)


numbers = [int(i) for i in input().split(', ')]
group_numbers(numbers)
