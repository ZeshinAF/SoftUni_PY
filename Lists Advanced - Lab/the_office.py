factored_employees = input().split(' ')
factor = int(input())

factored_employees = list(map(
    lambda x: int(x) * factor,
    factored_employees))

filtered_employees = list(filter(
    lambda x: x >= sum(factored_employees) / len(factored_employees),
    factored_employees))

happy_employees = len(filtered_employees)
if happy_employees >= len(factored_employees)/2:
    print(f"Score: {happy_employees}/{len(factored_employees)}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{len(factored_employees)}. Employees are not happy!")
