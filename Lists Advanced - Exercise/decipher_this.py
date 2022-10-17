def decipher(word):
    code = ''
    c = 0
    while word[c].isnumeric():
        code += word[c]
        c += 1
    message = word.replace(code, chr(int(code)))
    message = list(message)
    message[1], message[-1] = message[-1], message[1]
    return ''.join(message)


words = input().split(' ')
words = list(map(decipher, words))
for i in words:
    print(i, end=' ')
