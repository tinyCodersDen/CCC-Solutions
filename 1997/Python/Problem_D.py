sets = int(input())
while sets>=1:
    sets-=1
    l = []
    while True:
        k = input().split(' ')
        if k == ['']:
            break
        for e,t in enumerate(k):
            if t in l:
                k[e] = str(l.index(t)+1)
            else:
                l.append(t)
        print(' '.join(k))
    print('')
