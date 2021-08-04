# The problem name is "Sumac Sequences"
t1 = int(input(''))
t2 = int(input(''))
list1 = [t1,t2]
index = 0
while True:
    num = list1[index]
    num-= list1[index+1]
    if num >= 0:
        list1.append(num)
    else:
        break
    index+=1
print(len(list1))
