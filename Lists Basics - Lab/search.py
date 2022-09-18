words = []
n = int(input())
filter_word = input()
for _ in range(n):
    words.append(input())
print(words)
for i in range(len(words)-1, -1, -1):
    if filter_word not in words[i]:
        words.remove(words[i])
print(words)