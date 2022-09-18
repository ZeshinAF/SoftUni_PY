sequence = input().split(' ')
msg = input()
final = ''
for i in sequence:
    sum = 0
    for j in i:
        sum += int(j)
    if sum >= len(msg):
        c = msg[sum % (len(msg))]
        final += c
        msg = msg.replace(c, '',1)
    else:
        c = msg[sum]
        final += c
        msg = msg.replace(c, '',1)
print(final)
