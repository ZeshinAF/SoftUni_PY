def merge_items(words, start_index, end_index):
    if start_index < len(words):
        if end_index >= len(words):
            end_index = len(words) - 1
        result = []
        for i in range(start_index, end_index + 1):
            result.append(words[i])
        for i in result:
            words.remove(i)
        words.insert(start_index, ''.join(result))


def divide_items(words, index, partitions):
    pass


words = input().split(' ')
while True:
    command = input().split(' ')
    if command[0] == 'merge':
        start_index, end_index = int(command[1]), int(command[2])
        merge_items(words, start_index, end_index)
        print(words)
    elif command[0] == 'divide':
        index, partitions = int(command[1]), int(command[2])
        divide_items(words, index, partitions)

