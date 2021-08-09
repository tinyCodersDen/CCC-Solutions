x = int(input())
while True:
    x+=1
    stringx = str(x)
    a = []
    f = False
    for t in stringx:
        if t not in a:
            a.append(t)
        else:
            f=True
            break
    if f==False:
        print(x)
        break
