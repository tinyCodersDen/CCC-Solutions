num = int(input(''))
list1 = []
for u in range(num):
    ask = input('')
    x = ask.split(' ')
    x = [int(u) for u in x]
    list1.append(x)
a = 100
d = 100
for y in list1:
    if y[0]==y[1]:
        continue
    elif y[0]>y[1]:
        d-=y[0]
    elif y[0]<y[1]:
        a-=y[1]
print(a)
print(d)
