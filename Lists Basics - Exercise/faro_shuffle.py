deck = input().split(' ')
for _ in range(0, int(input())):
    shuffle = deck
    first_half = shuffle[0:len(deck) // 2]
    second_half = shuffle[len(deck) // 2:]
    f = 0
    s = 0
    for i in range(0, len(deck)):
        if i % 2 == 0:
            shuffle[i] = first_half[f]
            f+=1
        else:
            shuffle[i] = second_half[s]
            s+=1
    deck = shuffle
print(deck)