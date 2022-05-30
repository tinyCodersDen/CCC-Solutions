a = list(input())
b = input()
c = False
j = 0
for t in b:
    if t!='*':
        if t in a:
            a.remove(t)
        else:
            print('N')
            exit()
    else:
        c = True
        j+=1
if c==True:
    if len(a)==j:
        print('A')
        exit()
    else:
        print('N')
        exit()
print('A')
