for n in range(1,200+1):
    binnumber = bin(n)[2:]
    binnumber = binnumber[::-1]
    binnumber = binnumber[binnumber.find('1'):]
    if int(binnumber, 2) == 37:
        print(n)