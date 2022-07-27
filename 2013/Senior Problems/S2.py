W = int(input(''))
l = []
c = 0
b = False
for t in range(int(input(''))):
    g = int(input(''))
    l.append(g)
    if len(l)==5:
        l.pop(0)
        c+=1
    if sum(l)>W:
        print(c+len(l[:-1]))
        b = True
        break
if b==False:
    print(c+len(l))
