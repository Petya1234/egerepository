s = '>' + '1' * 15 + '2' * 20 + '3' * 8
while ('>1' in s) or ('>2' in s) or ('>3' in s):
    if '>1' in s:
        s = s.replace('>1', '41>', 1)
    if '>2' in s:
        s = s.replace('>2', '5>', 1)
    if '>3' in s:
        s = s.replace('>3', '44>', 1)
print(s.count('4'), s.count('1'), s.count('5'))