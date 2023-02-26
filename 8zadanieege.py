a = '012345678'
a1 = '02468'
a2 = '1357'
secondposition = 'АН'
fourposition = 'РМН'
end = 'ПОИНА'
wordlist = set()
counter = 0
for i1 in a1:
    for i2 in a2:
        for i3 in a1:
            for i4 in a2:
                for i5 in a1:
                    for i6 in a2:
                        for i7 in a1:
                            s = i1 + i2 + i3 + i4 +i5 +i6 + i7

                            counter += 1
print(counter)