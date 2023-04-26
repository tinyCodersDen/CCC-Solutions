def divisible(n):
    fours = 0
    fives = 0
    while True:
        if n%4==0 or n%5==0:
            if n%5==0:
                fives+=n//5
            elif n%4==0:
                fours+=n//4
            return [True,fours,fives]
        if n<0:
            return [False]
        n-=4
        fours+=1
k = divisible(int(input()))
if not k[0]:
    print(0)
    exit()
if k[1]<5:
    print(k[2]//4+1)
    exit()
if k[2]<4:
    print(k[1]//5+1)
else:
    print(k[1]//5+k[2]//4+1)
