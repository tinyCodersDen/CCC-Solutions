y = int(input(''))
t = list(map(int,input('').split(' ')))
r = list(map(int,input('').split(' ')))
sum1 = 0
for q,w in enumerate(r):
    s = t[q]+t[q+1]
    s=s/2
    s*=w
    sum1+=s
print(sum1)
