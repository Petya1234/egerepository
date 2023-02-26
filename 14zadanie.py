a = 223
s = ''
while a > 0:
    s = str(a % 31) + s
    a //= 31
print(s)