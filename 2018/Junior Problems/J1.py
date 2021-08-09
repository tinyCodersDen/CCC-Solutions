list1 = []
for x in range(4):
    ask = int(input(""))
    list1.append(ask)
if (list1[0]==8 or list1[0]==9) and (list1[1]==list1[2]) and (list1[3]==8 or list1[3]==9):
    print("ignore")
else:
    print('answer')
