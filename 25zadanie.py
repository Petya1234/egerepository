def checker_on_simple(n):
    t = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            t = 1
            break
    return t == 0
counter = 0
findvalues = []
for number in range(264871, 322989+1):
    numberdividers = []
    for dividers in range(2, int(number**0.5)+1):
        if number % dividers == 0 and checker_on_simple(dividers) == True:
            numberdividers.append(dividers)
    f = 0
    for i in range(len(numberdividers)-1):
        for j in range(i+1,len(numberdividers)):
            if numberdividers[i] * numberdividers[j] == number and str(numberdividers[i] % 10) == str(numberdividers[j] % 10):
                f = 1
                break
        if f == 1:
            counter+=1
            print(numberdividers, number)
            findvalues.append(number)
            break
print(counter, sum(findvalues)/ len(findvalues))