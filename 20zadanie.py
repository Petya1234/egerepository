def hod1(x):
    permit = False
    if hod2(x + 2) == True and x + 2 < 49:
        permit = True
    if hod2(x * 2) == True and x * 2 < 49:
        permit = True
    return permit
def hod2(x):
    permit = True
    if hod3(x + 2) == False or x + 2 >= 49:
        permit = False
    if hod3(x * 2) == False or x * 2 >= 49:
        permit = False
    return permit
def hod3(x):
    permit = False
    if x + 2 >= 49:
        permit = True
    if x * 2 >= 49:
        permit = True
    return permit
for i in range(1, 47+1):
    if hod1(i) == True:
        print(i)
