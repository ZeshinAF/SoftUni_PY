# def validate(x):
#     valid = True
#     if not 6 <= len(x) <= 10:
#         print("Password must be between 6 and 10 characters")
#         valid = False
#     if not x.isalnum():
#         print("Password must consist only of letters and digits")
#         valid = False
#     c = 0
#     a = 0
#     while c < 2 and a < len(x):
#         if x[a].isnumeric():
#             c += 1
#         a += 1
#     if c < 2:
#         print("Password must have at least 2 digits")
#         valid = False
#     if valid:
#         print("Password is valid")
def validate(x):
    c_len = False
    alnum = False
    atleast = False
    if 6 <= len(x) <= 10:
        c_len = True
    if x.isalnum():
        alnum = True
    c = 0
    for i in x:
        if i.isnumeric():
            c += 1
    if c >= 2:
        atleast = True
    if not c_len:
        print("Password must be between 6 and 10 characters")
    if not alnum:
        print("Password must consist only of letters and digits")
    if not atleast:
        print("Password must have at least 2 digits")
    if c_len and alnum and atleast:
        print("Password is valid")


passwd = input()
validate(passwd)
