list1 = []
for y in range(4):
    ask =input('')
    r = ask.split(' ')
    r = [int(t) for t in r]
    list1.append(r)
num = 0
for x in list1:
    if num == 0:
        for u in x:
            num+=u
    else:
        num2 = 0
        for u in x:
            num2+=u
        if num2==num:
            pass
        else:
            print('not magic')
            exit()
index = 0
for s in range(4):
    num2 = 0
    for x in list1:
        num2+=x[s]
    if num2 == num:
        pass
    else:
        print('not magic')
        print(x)
        exit()
print('magic')
