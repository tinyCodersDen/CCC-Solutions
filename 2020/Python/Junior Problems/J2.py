list1 = []
for m in range(3):
    ask = int(input(''))
    list1.append(ask)
count = 0
num = list1[1]
num2 = list1[1]
for n in range(100000000000):
    count+=1
    num2=num2*list1[2]
    num+=num2
    if num>list1[0]:
        print(count)
        exit()
