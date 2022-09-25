text = input().split(' ')
palindrome = input()
words = [i for i in text if i == ''.join(reversed(i))]
print(words)
c = 0
while palindrome in words:
    c += 1
    words.remove(palindrome)
print(f'Found palindrome {c} times')
