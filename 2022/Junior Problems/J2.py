r = int(input())
p = 0
for t in range(r):
    s = int(input())
    f = int(input())
    a = (5*s)-(3*f)
    if a>40:
        p+=1
if p==r:
    print(str(p)+'+')
else:
    print(p)
