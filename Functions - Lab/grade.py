def solve(x):
    if 5.50 <= x <= 6:
        return 'Excellent'
    elif 4.50 <= x <= 5.49:
        return 'Very Good'
    elif 3.50 <= x <= 4.49:
        return 'Good'
    elif 3.00 <= x <= 3.49:
        return 'Poor'
    elif 2.00 <= x <= 2.99:
        return 'Fail'


grade = float(input())
print(solve(grade))
