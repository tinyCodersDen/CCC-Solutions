l=[]
for t in range(int(input())):
    c = int(input(''))
    if c!=0:
        l.append(c)
    else:
        l.pop(-1)
print(sum(l))
