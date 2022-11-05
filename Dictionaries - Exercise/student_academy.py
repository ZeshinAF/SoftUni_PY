n = int(input())
students = {}
for _ in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)
for k, v in students.items():
    average = sum(v) / len(v)
    if average >= 4.5:
        print(f"{k} -> {average:.2f}")
