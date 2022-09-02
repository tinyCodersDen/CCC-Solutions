while True:
    k = int(input())
    if k==0:
        break
    minimum = [0,0]
    p = 100000000000000000000
    for t in range(1,k//2+1):
        if k/t==int(k/t) and ((k//t)*2)+(t*2)<p:
            p = ((k//t)*2)+(t*2)
            minimum = [k//t,t]
    minimum.sort()
    print('Minimum perimeter is',p,'with dimensions',minimum[0],'x',minimum[1])
