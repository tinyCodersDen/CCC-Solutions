n = int(input(''))
l = []
for t in range(n):
    v = list(map(int,input().split(' ')))
    l.append(v)
l = sorted(l, key = lambda x: x[0])
max_avg = 0
for e,t in enumerate(l):
    if e != len(l)-1:
        average = (abs(t[1]-l[e+1][1]))/abs(t[0]-l[e+1][0])
        if average>max_avg:
            max_avg = average
print(max_avg)
