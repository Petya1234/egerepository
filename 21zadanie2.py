def hod1(x, y):
    permit = True
    if hod2(x + 2, y) == False or x + 2 + y >= 94:
        permit = False
    if hod2(x * 4, y) == False or x * 4 + y >= 94:
        permit = False
    if hod2(x, y + 2) == False or x + y + 2 >= 94:
        permit = False
    if hod2(x, y * 4) == False or x + y * 4 >= 94:
        permit = False
    return permit
def hod2(x, y):
    permit = False
    if hod3(x + 2, y) == True or x + 2 + y >= 94:
        permit = True
    if hod3(x * 4, y) == True or x * 4 + y >= 94:
        permit = True
    if hod3(x, y + 2) == True or x + y + 2 >= 94:
        permit = True
    if hod3(x, y * 4) == True or x + y * 4 >= 94:
        permit = True
    return permit
def hod3(x, y):
    permit = True
    if hod4(x + 2, y) == False or x + 2 + y >= 94:
        permit = False
    if hod4(x * 4, y) == False or x * 4 + y >= 94:
        permit = False
    if hod4(x, y + 2) == False or x + y + 2 >= 94:
        permit = False
    if hod4(x, y * 4) == False or x + y * 4 >= 94:
        permit = False
    return permit
def hod4(x, y):
    permit = False
    if x + 2 + y >= 94:
        permit = True
    if x * 4 + y >= 94:
        permit = True
    if x + y + 2 >= 94:
        permit = True
    if x + y * 4 >= 94:
        permit = True
    return permit

def hod1t(x, y):
    permit = True
    if hod2t(x + 2, y) == False or x + 2 + y >= 94:
        permit = False
    if hod2t(x * 4, y) == False or x * 4 + y >= 94:
        permit = False
    if hod2t(x, y + 2) == False or x + y + 2 >= 94:
        permit = False
    if hod2t(x, y * 4) == False or x + y * 4 >= 94:
        permit = False
    return permit
def hod2t(x, y):
    permit = False
    if x + 2 + y >= 94:
        permit = True
    if x * 4 + y >= 94:
        permit = True
    if x + y + 2 >= 94:
        permit = True
    if x + y * 4 >= 94:
        permit = True
    return permit

for i in range(1, 89+1):
    if hod1(4, i) == True and hod1t(4, i) == False:
        print(i)
        exit()