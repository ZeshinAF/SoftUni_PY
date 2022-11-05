n = int(input())
parked_cars = {}
for _ in range(n):
    command = input().split(' ')
    if command[0] == 'register':
        username, license_plate = command[1], command[2]
        if username not in parked_cars:
            parked_cars[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parked_cars[username]}")
    elif command[0] == 'unregister':
        username = command[1]
        if username in parked_cars:
            parked_cars.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
for k, v in parked_cars.items():
    print(f"{k} => {v}")
