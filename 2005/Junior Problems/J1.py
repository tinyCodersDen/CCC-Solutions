Day = int(input(''))
Evening = int(input(''))
weekend = int(input(''))
Ac = (Day-100)*25
Bc = (Day-250)*45
if Ac<=0:
    Ac = 0
if Bc<=0:
    Bc = 0
A = ((Ac)+(15*Evening)+(20*weekend))/100
B = ((Bc)+(35*Evening)+(25*weekend))/100
pa = str(A).split('.')
pb = str(B).split('.')
if len(pa[1])==1:
    pa[1]+='0'
if len(pb[1])==1:
    pb[1]+='0'
A = '.'.join(pa)
B = '.'.join(pb)
print('Plan A costs',A)
print('Plan B costs',B)
if float(A)<float(B):
    print('Plan A is cheapest.')
elif float(A)>float(B):
    print('Plan B is cheapest.')
else:
    print('Plan A and B are the same price.')
