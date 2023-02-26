def hod1(x, y):
    permit = False
    if hod2(x + 1, y) == True and x + 1 + y < 231:
        permit = True
    if hod2(x * 2, y) == True and x * 2 + y < 231:
        permit = True
    if hod2(x, y + 1) == True and x + y + 1 < 231:
        permit = True
    if hod2(x, y * 2) == True and x + y * 2 < 231:
        permit = True
    return permit
def hod2(x, y):
    permit = False
    if x + 1 + y >= 231:
        permit = True
    if x * 2 + y >= 231:
        permit = True
    if x + y + 1 >= 231:
        permit = True
    if x + y * 2 >= 231:
        permit = True
    return permit
for i in range(1, 214):
    if hod1(17, i) == True:
        print(i)
        exit()