company_users = {}
while True:
    command = input()
    if command == 'End':
        break
    company_name, id = command.split(' -> ')
    if company_name not in company_users:
        company_users[company_name] = []
    if id not in company_users[company_name]:
        company_users[company_name].append(id)
for k, v in company_users.items():
    print(k)
    for i in v:
        print(f"-- {i}")
