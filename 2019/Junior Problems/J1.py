l = []
for m in range(6):
    ask = int(input(''))
    l.append(ask)
s1 = (3*l[0])+(2*l[1])+(1*l[2])
s2 = (3*l[3])+(2*l[4])+(1*l[5])
if s1>s2:
    print('A')
elif s2>s1:
    print('B')
else:
    print('T')
