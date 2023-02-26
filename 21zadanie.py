def hod1(x):
    permit = True
    if hod2(x + 2) == False or x + 2 >= 49:
        permit = False
    if hod2(x * 2) == False or x * 2 >= 49:
        permit = False
    return permit
def hod2(x):
    permit = False
    if hod3(x + 2) == True or x + 2 >= 49:
        permit = True
    if hod3(x * 2) == True or x * 2 >= 49:
        permit = True
    return permit
def hod3(x):
    permit = True
    if hod4(x + 2) == False or x + 2 >= 49:
        permit = False
    if hod4(x * 2) == False or x * 2 >= 49:
        permit = False
    return permit
def hod4(x):
    permit = False
    if x + 2 >= 49:
        permit = True
    if x * 2 >= 49:
        permit = True
    return permit

def hod1t(x):
    permit = True
    if hod2t(x + 2) == False or x + 2 >= 49:
        permit = False
    if hod2t(x * 2) == False or x * 2 >= 49:
        permit = False
    return permit
def hod2t(x):
    permit = False
    if x + 2 >= 49:
        permit = True
    if x * 2 >= 49:
        permit = True
    return permit

for i in range(1, 47+1):
    if hod1(i) == True and hod1t(i) == False:
        print(i)
        exit()