ask = input("")
list1 = [1,2,3,4]
for x in ask:
    if "H"==x:
        list1[1],list1[3] = list1[3],list1[1]
        list1[0],list1[2] = list1[2],list1[0]
    if "V"==x:
        list1[0],list1[1] = list1[1],list1[0]
        list1[2],list1[3] = list1[3],list1[2]
print (list1[0],list1[1])
print(list1[2],list1[3])
