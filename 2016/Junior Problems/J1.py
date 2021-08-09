list1 = []
for y in range(6):
    ask =input('')
    list1.append(ask)
count1 = 0
for u in list1:
    if u == "W":
        count1+=1
if count1 == 0:
    print(-1)
elif count1==1 or count1==2:
    print(3)
elif count1==3 or count1==4:
    print(2)
elif count1==5 or count1==6:
    print(1)
