# def fill_electrons(electrons):
#     shells = []
#     shell = 1
#     while electrons != 0:
#         max_capacity = 2 * shell * shell
#         if electrons >= max_capacity:
#             shells.append(max_capacity)
#             electrons -= max_capacity
#         else:
#             shells.append(electrons)
#             electrons = 0
#         shell += 1
#     return shells
def fill_electrons(electrons):
    shells = []
    shell = 1
    capacity = 2 * shell * shell
    while electrons >= capacity:
        shells.append(capacity)
        electrons -= capacity
        shell += 1
        capacity = 2 * shell * shell
    else:
        shells.append(electrons)
    return shells


e = int(input())
electron_shells = fill_electrons(e)
print(electron_shells)
