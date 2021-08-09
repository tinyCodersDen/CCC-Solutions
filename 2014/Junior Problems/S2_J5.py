num = int(input(''))
list1 = []
ask = input('')
ask2 = input('')
x,y = ask.split(' '),ask2.split(' ')
for i in range(len(x)):
    list1.append([x[i],y[i]])
for a in range(num):
    for s in list1:
        if [s[1],s[0]] in list1 and s[0]!=s[1]:
            pass
        else:
            print('bad')
            exit()
print('good')
