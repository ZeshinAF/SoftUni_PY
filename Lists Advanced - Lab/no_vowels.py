vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
text = ''.join([i for i in text if i.lower() not in vowels])
print(text)
