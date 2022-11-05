message = list(input())
numbers_list = []
non_numbers_list = []

for i in message:
    if i.isnumeric():
        numbers_list.append(i)
    else:
        non_numbers_list.append(i)
take_list = []
skip_list = []
for i in range(0, len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

