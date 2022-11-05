n = int(input())
words = {}
for _ in range(n):
    word = input()
    synonym = input()
    if word in words:
        words[word].append(synonym)
    else:
        words[word] = [synonym]
for k, v in words.items():
    print(f"{k} - {', '.join(v)}")
