while True:
    name = input()

    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    a = len(name)
    if a < 5:
        print(f"{name} goes to Gryffindor.")
    elif a == 5:
        print(f"{name} goes to Slytherin.")
    elif a == 6:
        print(f"{name} goes to Ravenclaw.")
    elif a > 6:
        print(f"{name} goes to Hufflepuff.")