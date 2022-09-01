n = int(input(''))
m = int(input(''))
l = []
l2 = []
for y in range(n):
    l.append(input(''))
for z in range(m):
    l2.append(input(''))
for q in l:
    for z in l2:
        print(q,'as',z)
