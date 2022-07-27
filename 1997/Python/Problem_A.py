for g in range(int(input(''))):
    s = int(input(''))
    v = int(input(''))
    o = int(input(''))
    l1 = []
    l2 = []
    l3 = []
    for n in range(s):
        l1.append(input(''))
    for n in range(v):
        l2.append(input(''))
    for n in range(o):
        l3.append(input(''))
    for t in l1:
        for g in l2:
            for k in l3:
                print(t+' '+g+' '+k+'.')
