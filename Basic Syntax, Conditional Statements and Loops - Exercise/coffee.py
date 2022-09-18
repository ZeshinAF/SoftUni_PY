upper_events = ["CODING", "DOG", "CAT", "MOVIE"]
lower_events = ["coding", "dog", "cat", "movie"]
a = input()
c = 0
while a != 'END':
    if a in lower_events:
        c += 1
    elif a in upper_events:
        c += 2
    a = input()
if c > 5:
    print("You need extra sleep")
else:
    print(c)
