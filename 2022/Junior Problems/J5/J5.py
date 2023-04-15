# This one earns 8/15
import copy
yard = int(input())
trees  = []
for t in range(int(input())):
    trees.append(list(map(int,input('').split(' '))))
for p in range(yard-1,0,-1):
    s = [1,1]
    end = [copy.copy(p),copy.copy(p)]
    while True:
        if end==[yard,yard]:
            break
        fit = True 
        for t in trees:
            if t[0]>=s[0] and t[0]<=end[0] and t[1]>=s[1] and t[1]<=end[1]:
                fit = False
                break
        if fit:
            print(p)
            exit()
        if end[1]==yard:
            s = [s[0]+1,1]
            end = [end[0]+1,copy.copy(p)]
        s[1]+=1
        end[1]+=1
