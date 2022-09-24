def palindrome(x):
    num = str(x)
    c = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] != num[c]:
            break
        c += 1
    else:
        return True
    return False


numbers = [print(palindrome(int(i))) for i in input().split(', ')]
