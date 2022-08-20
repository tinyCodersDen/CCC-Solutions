cr = list(map(int,input('').split(' ')))
cursor = [0,0]
while True:
    f = list(map(int,input('').split(' ')))
    if f==[0,0]:
        break
    if f[0]+cursor[0]<=cr[0]:
        if 0<=f[0]+cursor[0]:
            cursor[0]+=f[0]
        else:
            cursor[0] = 0
    else:
        cursor[0] = cr[0]
    if f[1]+cursor[1]<=cr[1]:
        if 0<=f[1]+cursor[1]:
            cursor[1]+=f[1]
        else:
            cursor[1] = 0
    else:
        cursor[1] = cr[1]
    print(cursor[0],cursor[1])
