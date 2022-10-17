def some_positives(some_numbers):
    return [str(i) for i in some_numbers if i >= 0]


def some_negatives(some_numbers):
    return [str(i) for i in some_numbers if i < 0]


def some_evens(some_numbers):
    return [str(i) for i in some_numbers if i % 2 == 0]


def some_odds(some_numbers):
    return [str(i) for i in some_numbers if i % 2 != 0]


numbers = [int(i) for i in input().split(', ')]
print(f'Positive: {", ".join(some_positives(numbers))}')
print(f'Negative: {", ".join(some_negatives(numbers))}')
print(f'Even: {", ".join(some_evens(numbers))}')
print(f'Odd: {", ".join(some_odds(numbers))}')

