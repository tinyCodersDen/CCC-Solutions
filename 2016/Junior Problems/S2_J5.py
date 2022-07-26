question = int(input())
l = int(input())
dmoj = list(map(int,input('').split(' ')))
peg = list(map(int,input('').split(' ')))
if question==1:
    dmoj.sort()
    peg.sort()
    ans = 0
    for e,t in enumerate(dmoj):
        ans+=max([t,peg[e]])
    print(ans)
elif question==2:
    dmoj.sort()
    peg.sort()
    dmoj = dmoj[::-1]
    ans = 0
    for e,t in enumerate(dmoj):
        ans+=max([t,peg[e]])
    print(ans)
