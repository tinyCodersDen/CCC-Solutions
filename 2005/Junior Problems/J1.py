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
print('Plan A costs',A)
print('Plan B costs',B)
if A<B:
    print('Plan A is cheapest.')
elif A>B:
    print('Plan B is cheapest.')
else:
    print('Plan A and B are the same price.')
