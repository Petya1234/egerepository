for a in range(10000,1,-1):
    f = 0
    for x in range(1,10000):
        if (((x & 13 != 0) or (x & 13 == 0)) <= ((x & a != 0) or (x & 39 == 0))) == False:
            f = 1
            break
    if f == 0:
        print(a)
