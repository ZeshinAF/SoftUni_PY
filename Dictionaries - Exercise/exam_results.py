exam_results = {}
submissions = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    elif '-banned' in command:
        username = command.replace('-banned', '')
        if username in exam_results:
            exam_results.pop(username)
    else:
        name, language, points = command.split('-')
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        if name in exam_results:
            if int(points) > exam_results[name]:
                exam_results[name] = int(points)
        else:
            exam_results[name] = int(points)
print("Results:")
for k, v in exam_results.items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in submissions.items():
    print(f"{k} - {v}")
