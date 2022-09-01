n = 1
s = [[54,19],[90,48],[99,77]]
l = [[9,34],[40,64],[67,86]]
while True:
    i = int(input())
    if i==0:
        print('You Quit!')
        break
    if n+i<100:
        n+=i
        for t in range(3):
            if n==l[t][0]:
                n = l[t][1]
            if n==s[t][0]:
                n = s[t][1]
    if n+i==100:
        print('You are now on square 100')
        print('You Win!')
        break
    print('You are now on square',n)
