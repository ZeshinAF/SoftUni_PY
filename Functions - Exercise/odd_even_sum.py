def odd_even_sum(x):
    even = 0
    odd = 0
    for i in x:
        num = int(i)
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return f'Odd sum = {odd}, Even sum = {even}'


number = input()
print(odd_even_sum(number))
