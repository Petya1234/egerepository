def hod1(x, y):
    permit = True
    if hod2(x + 3, y) == False or x + 3 + y >= 80:
        permit = False
    if hod2(x * 2, y) == False or x * 2 + y >= 80:
        permit = False
    if hod2(x, y + 3) == False or x + y + 3 >= 80:
        permit = False
    if hod2(x, y * 2) == False or x + y * 2 >= 80:
        permit = False
    return permit
def hod2(x, y):
    permit = False
    if hod3(x + 3, y) == True or x + 3 + y >= 80:
        permit = True
    if hod3(x * 2, y) == True or x * 2 + y >= 80:
        permit = True
    if hod3(x, y + 3) == True or x + y + 3 >= 80:
        permit = True
    if hod3(x, y * 2) == True or x + y * 2 >= 80:
        permit = True
    return permit
def hod3(x, y):
    permit = True
    if hod4(x + 3, y) == False or x + 3 + y >= 80:
        permit = False
    if hod4(x * 2, y) == False or x * 2 + y >= 80:
        permit = False
    if hod4(x, y + 3) == False or x + y + 3 >= 80:
        permit = False
    if hod4(x, y * 2) == False or x + y * 2 >= 80:
        permit = False
    return permit
def hod4(x, y):
    permit = False
    if x + 3 + y >= 80:
        permit = True
    if x * 2 + y >= 80:
        permit = True
    if x + y + 3 >= 80:
        permit = True
    if x + y * 2 >= 80:
        permit = True
    return permit

def hod1t(x, y):
    permit = True
    if hod2t(x + 3, y) == False or x + 3 + y >= 80:
        permit = False
    if hod2t(x * 2, y) == False or x * 2 + y >= 80:
        permit = False
    if hod2t(x, y + 3) == False or x + y + 3 >= 80:
        permit = False
    if hod2t(x, y * 2) == False or x + y * 2 >= 80:
        permit = False
    return permit
def hod2t(x, y):
    permit = False
    if x + 3 + y >= 80:
        permit = True
    if x * 2 + y >= 80:
        permit = True
    if x + y + 3 >= 80:
        permit = True
    if x + y * 2 >= 80:
        permit = True
    return permit

for i in range(1, 71+1):
    if hod1(8, i) == True and hod1t(8, i) == False:
        print(i)