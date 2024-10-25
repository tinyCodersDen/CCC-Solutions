for h in range(T):
    j = input()
    d = {}
    for t in j:
        if t in d.keys():
            d[t] += 1
        else:
            d[t] = 1
    if d[j[0]] == 1:
        b = False
        for t in range(0,len(j),2):
            if d[j[t]]!=1:
                b = True
                print('F')
                break
        if not b:
            b = False
            for t in range(1,len(j),2):
                if d[j[t]]<2:
                    b = True
                    print('F')
                    break
            if not b:
                print("T")
    elif d[j[0]]>1:
        b = False
        for t in range(0,len(j),2):
            if d[j[t]]<2:
                b = True
                print('F')
                break
        if not b:    
            b = False
            for t in range(1,len(j),2):
                if d[j[t]]!=1:
                    b = True
                    print('F')
                    break
            if not b:
                print("T")
