# This one earns 14/15
import copy
same = []
differ = []
for t in range(int(input())):
    same.append(input().split(' '))
for t in range(int(input())):
    differ.append(input().split(' '))
ans = 0
l = []
for t in range(int(input())):
    l.append(input().split(' '))
for y in l:
    n = copy.copy(same)
    for t in same:
        if t[0] in y and t[1] not in y:
            ans+=1
            n.remove(t)
        elif t[1] in y and t[0] not in y:
            ans+=1
            n.remove(t)
    same = copy.copy(n)
for h in l:
    n = copy.copy(differ)
    for r in differ:
        if r[0] in h and r[1] in h:
            ans+=1
            n.remove(r)
    differ = copy.copy(n)
print(ans)
