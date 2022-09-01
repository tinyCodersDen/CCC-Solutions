a1,a = '',1000000000
while True:
    k = input('').split(' ')
    if int(k[1])<a:
        a = int(k[1])
        a1 = k[0]
    if k[0]=='Waterloo':
        print(a1)
        break
