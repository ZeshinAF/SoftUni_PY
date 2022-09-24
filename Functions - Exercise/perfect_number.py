def perfect_number(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    if sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


x = int(input())
print(perfect_number(x))