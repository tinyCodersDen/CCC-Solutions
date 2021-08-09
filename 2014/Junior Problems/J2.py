ask = input('')
list1 = []
ask = input('')
list1 = list(ask)
a = 0
b = 0
for u in list1:
    if u=='A':
        a+=1
    else:
        b+=1
if a>b:
    print('A')
elif b>a:
    print('B')
else:
    print('Tie')
