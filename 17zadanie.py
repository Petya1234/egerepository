f = open('../ege/17.ege.txt')
a = [int(x) for x in f]
def in_triple(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x //= 3
    return sum(list(map(int,list(s))))
counter = 0
values = []
mx = a[0]
for i in range(len(a)):
    if a[i] > mx and a[i] % 11 == 0:
        mx = a[i]

mx = in_triple(mx)

for i in range(len(a)-1):
    A = a[i]
    B = a[i+1]
    if (in_triple(A) == mx or in_triple(B) == mx):
        values.append(A + B)
        counter += 1
print(counter, min(values))