list1 = []
for x in range(2):
    ask = int(input(''))
    list1.append(ask)
var1 = list1[0]
var2 = list1[0]*10
for x in range(list1[1]):
    var1=var1+var2
    var2=var2*10
print(var1)
