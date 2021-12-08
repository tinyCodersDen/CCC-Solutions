fav_team = int(input(''))
dict1 = {1:0,2:0,3:0,4:0}
list1 = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
q = int(input(''))
for t in range(q):
    a,b,sa,sb=list(map(int,input('').split(' ')))
    if sa>sb:
        dict1[a]+=3
    elif sa<sb:
        dict1[b]+=3
    elif sa==sb:
        dict1[a]+=1
        dict1[b]+=1
    if [a,b] in list1:
        list1.remove([a,b])
    if [b,a] in list1:
        list1.remove([b,a])
def check(remaining_games):
    total=0
    if remaining_games==3:
        for t in range(3):
            for a in range(3):
                for e in range(3):
                    test_dict = dict1.copy()
                    for xz,q in enumerate([t,a,e]):
                        if q==0:
                            win_team = list1[xz][0]
                            test_dict[win_team]+=3
                            v = list(test_dict.values())
                            v.remove(test_dict[fav_team])
                            if test_dict[fav_team]>max(v):
                                total+=1
                        elif q==1:
                            test_dict[list1[xz][1]]+=3
                            v = list(test_dict.values())
                            v.remove(test_dict[fav_team])
                            if test_dict[fav_team]>max(v):
                                total+=1
                        else:
                            test_dict[list1[1][0]]+=1
                            test_dict[list1[1][1]]+=1
                            v = list(test_dict.values())
                            v.remove(test_dict[fav_team])
                            if test_dict[fav_team]>max(v):
                                total+=1
    if remaining_games==1:
        for a in range(3):
            test_dict = dict1
            if a==0:
                test_dict[list1[0][0]]+=3
                v = list(test_dict.values())
                v.remove(test_dict[fav_team])
                if test_dict[fav_team]>max(v):
                    total+=1
            elif a==1:
                test_dict[list1[0][1]]+=3
                v = list(test_dict.values())
                v.remove(test_dict[fav_team])
                if test_dict[fav_team]>max(v):
                    total+=1
            else:
                test_dict[list1[0][0]]+=1
                test_dict[list1[0][1]]+=1
                v = list(test_dict.values())
                v.remove(test_dict[fav_team])
                if test_dict[fav_team]>max(v):
                    total+=1
    testcount = 0
    if remaining_games==5:
        for first in range(3):
            for second in range(3):
                for third in range(3):
                    for fourth in range(3):
                        for fifth in range(3):
                            test_dict = dict1.copy()
                            for xz,q in enumerate([first,second,third,fourth,fifth]):

                                if q==0:
                                    test_dict[list1[xz][0]]+=3
                                    # v = list(test_dict.values())
                                    # v.remove(test_dict[fav_team])
                                    # if test_dict[fav_team]>max(v):
                                    #     total+=1
                                if q==1:
                                    test_dict[list1[xz][1]]+=3
                                    # v = list(test_dict.values())
                                    # v.remove(test_dict[fav_team])
                                    # if test_dict[fav_team]>max(v):
                                    #     total+=1
                                if q==2:
                                    test_dict[list1[xz][0]]+=1
                                    test_dict[list1[xz][1]]+=1
                                    # v = list(test_dict.values())
                                    # v.remove(test_dict[fav_team])
                                    # if test_dict[fav_team]>max(v):
                                    #     total+=1
                                if xz==4:
                                    v = list(test_dict.values())
                                    v.remove(test_dict[fav_team])
                                    if test_dict[fav_team]>max(v):
                                        total+=1
    if remaining_games==6:
        for first in range(3):
            for second in range(3):
                for third in range(3):
                    for fourth in range(3):
                        for fifth in range(3):
                            for sixth in range(3):
                                test_dict = dict1.copy()
                                for xz,q in enumerate([first,second,third,fourth,fifth,sixth]):
                                    if q==0:
                                        test_dict[list1[xz][0]]+=3
                                        # v = list(test_dict.values())
                                        # v.remove(test_dict[fav_team])
                                        # if test_dict[fav_team]>max(v):
                                        #     total+=1
                                    if q==1:
                                        test_dict[list1[xz][1]]+=3
                                        # v = list(test_dict.values())
                                        # v.remove(test_dict[fav_team])
                                        # if test_dict[fav_team]>max(v):
                                        #     total+=1
                                    if q==2:
                                        test_dict[list1[xz][0]]+=1
                                        test_dict[list1[xz][1]]+=1
                                        # v = list(test_dict.values())
                                        # v.remove(test_dict[fav_team])
                                        # if test_dict[fav_team]>max(v):
                                        #     total+=1
                                    if xz==5:
                                        v = list(test_dict.values())
                                        v.remove(test_dict[fav_team])
                                        if test_dict[fav_team]>max(v):
                                            total+=1               
    print(total)
    check(6-q)
