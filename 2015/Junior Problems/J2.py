list1 = []
ask = input('')
for u in ask:
    list1.append(u)
sad = 0
happy = 0
for i,y in enumerate(list1):
    try:
        if y==':' and list1[i+1]=='-' and list1[i+2]==')':
            happy+=1
        if y==':' and list1[i+1]=='-' and list1[i+2]=='(':
            sad+=1
    except IndexError:
        pass
if happy>sad:
    print("happy")
elif sad>happy:
    print('sad')
elif sad==0 and happy==0:
    print("none")
elif sad==happy:
    print('unsure')
