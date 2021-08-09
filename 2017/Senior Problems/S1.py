x = int(input(''))
s = list(map(int,input('').split(' ')))
w = list(map(int,input('').split(' ')))
s1 = sum(s)
s2 = sum(w)
for t in range(x-1,-1,-1):
    if s1==s2:
        print(t+1)
        exit()
    s1-=s[t]
    s2-=w[t]
print(0)
