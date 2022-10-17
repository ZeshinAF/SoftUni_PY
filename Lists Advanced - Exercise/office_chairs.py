def check_rooms(rooms):
    needed_chairs = 0
    free_chairs = 0
    for room in range(1, rooms+1):
        chairs, visitors = input().split(' ')
        diff = len(chairs) - int(visitors)
        if diff < 0:
            needed_chairs += abs(diff)
            print(f'{abs(diff)} more chairs needed in room {room}')
        else:
            free_chairs += abs(diff)
    return needed_chairs, free_chairs


n = int(input())
needed, free = check_rooms(n)
if free >= needed:
    print(f'Game On, {free-needed} free chairs left')
