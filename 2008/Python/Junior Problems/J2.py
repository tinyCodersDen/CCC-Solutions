l = ['A','B','C','D','E']
while True:
    b = int(input())
    n = int(input())
    if b==4 and n==1:
        print(' '.join(l))
        break
    if b==1:
        for t in range(n):
            l.append(l[0])
            l.pop(0)
    elif b==2:
        for t in range(n):
            l.insert(0,l[-1])
            l.pop(-1)
    elif b==3:
        for t in range(n):
            l[0],l[1] = l[1],l[0]
