def solve(first, second, operation):
    if operation == 'multiply':
        return first * second
    elif operation == 'divide':
        return int(first / second)
    elif operation == 'add':
        return first + second
    elif operation == 'subtract':
        return first - second


operation = input()
first = int(input())
second = int(input())
print(solve(operation=operation, first=first, second=second))
