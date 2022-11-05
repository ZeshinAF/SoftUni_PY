contacts = {}
while True:
    contact = input()
    if '-' not in contact:
        break
    name, number = contact.split('-')
    contacts[name] = number
for _ in range(int(contact)):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
