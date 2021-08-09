list1 = []
for x in range(2):
    ask = int(input(''))
    list1.append(ask)
if list1[0]>=1 and list1[1]>=1:
    print(1)
if list1[0]<=-1 and list1[1]>=1:
    print(2)
if list1[0]<=-1 and list1[1]<=-1:
    print(3)
if list1[0]>=1 and list1[1]<=-1:
    print(4)
