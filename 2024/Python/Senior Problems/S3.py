# This submission yields 4/15 points
import copy
N = int(input())

a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))

if N==2:
    if (a[0] not in b) and (a[1] not in b):
        print("NO")
    else:
        if a[0] == b[1] and a[1] == b[0] and a!=b:
            print("NO")
        elif (b[0] not in a) or (b[1] not in a):
            print("NO")
        else:
            print("YES")
            if set(a) == set(b):
                print(0)
            else:
                print('1')
                if a[0] in b:
                    print('R 0 1')
                elif a[1] in b:
                    print('L 0 1')
else:
    if a == b:
        print("YES")
        print(0)
    else:
        z = False
        for f in b:
            if f not in a:
                print("NO")
                z = True
                break
        if not z:
            i = 0
            ans = []
            for e in range(len(a)):
                if a[e] != b[e]:
                    z = False
                    for q in range(e+1,len(a)):
                        if a[e:q][::-1] == b[e:q]:
                            z = True
                            break
                    if z:
                        print("NO")
                        break
                    if not z:
                        if a[e-1] == b[e-1] and a[e-1] == b[e] and e!=0:
                            for q in range(e,len(a)):
                                if b[q] != b[e-1]:
                                    q-=1
                                    break
                                a[q] = a[e-1]
                            ans.append("R "+str(e-1)+" "+str(q))
                            i+=1
                        else:
                            for q in range(e,len(a)):
                                if a[q] == b[q]:
                                    break
                            for w in range(q,e-1,-1):
                                a[w] = copy.copy(a[q]) 
                            ans.append("L "+str(e)+" "+str(q))
                            i+=1
            if not z:
                print("YES")
                print(i)
                for t in ans:
                    print(t)
