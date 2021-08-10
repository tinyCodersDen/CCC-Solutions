ask = int(input(''))
list1 = []
for k in range(ask):
    ask2 = input('')
    cv = ask2.split(',')
    cv = [int(l) for l in cv]
    list1.append(cv)
list2 = [[],[],[],[]]
minx,miny,maxx,maxy = 1000,1000,0,0
for n in list1:
    k = n
    if k[1]<miny:
        miny=k[1]
        list2[1]=k
    if k[0]<minx:
        minx=k[0]
        list2[0]=k
    if k[0]>maxx:
        maxx=k[0]
        list2[2]=k
    if k[1]>maxy:
        maxy=k[1]
        list2[3]=k
num1 = [list2[0][0]-1,list2[1][1]-1]
num2 = [list2[2][0]+1,list2[3][1]+1]
print(str(num1[0])+','+str(num1[1]))
print(str(num2[0])+','+str(num2[1]))
