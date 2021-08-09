list1 = []
for y in range(2):
    ask = int(input(''))
    list1.append(ask)
if list1[0]<=2:
    if list1[0]==2 and list1[1]<18:
        print('Before')
    elif list1[0]<2:
        print("Before")
if list1[0]==2 and list1[1]==18:
    print('Special')
    exit()
if list1[0]>=2:
    if list1[0]==2 and list1[1]>18:
        print('After')
    elif list1[0]>2:
        print("After")
