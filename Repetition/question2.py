a = 10
b = 50
c = 0
for i in range(a, b):
    d = 0
    if c == 0:
        c = a
    else:
        d = c + i
        c = d
    print(c)