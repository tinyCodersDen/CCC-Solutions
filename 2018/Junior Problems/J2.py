list1 = []
list2 = []
ask = input('')
ask = input("")
for y in ask:
    list1.append(y)
ask = input("")
for y in ask:
    list2.append(y)
count = 0
for x,i in enumerate(list1):
    if i=='C' and list2[x]=="C":
        count+=1
print(count)
