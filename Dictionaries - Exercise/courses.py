courses = {}
while True:
    command = input()
    if command == 'end':
        break
    course_name, student_name = command.split(' : ')
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
for k, v in courses.items():
    print(f"{k}: {len(v)}")
    for i in v:
        print(f"-- {i}")
