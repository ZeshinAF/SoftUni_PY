force_book = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    sides = force_book.keys()
    users_lists = force_book.values()
    if '|' in command:
        force_side, force_user = command.split(' | ')
        for i in users_lists:
            if force_user in i:
                break
        else:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        for k, v in force_book.items():
            for i in v:
                if force_user == i:
                    force_book[k].remove(force_user)
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
for k, v in force_book.items():
    member_count = len(v)
    if member_count > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for i in v:
            print(f"! {i}")
