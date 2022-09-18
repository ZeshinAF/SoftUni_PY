key = int(input())
n = int(input())
msg = ''
for i in range(0,n):
    msg += chr(ord(input()) + key)
print(msg)