s = int(input(''))
e = int(input(''))
for q in range(s,e+1):
    z = q-s
    if z%4==0 and z%2==0 and z%3==0 and z%5==0:
        print('All positions change in year',q)
