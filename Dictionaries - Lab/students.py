students = {}
student = input().split(':')
while len(student) > 1:
    name = student[0]
    id = student[1]
    course = student[2]
    if course in students:
        students[course].update({id: name})
    else:
        students[course] = {id: name}
    student = input().split(':')
for i in students:
    if i == student[0].replace('_', " "):
        for k, v in students[i].items():
            print(f"{v} - {k}")
