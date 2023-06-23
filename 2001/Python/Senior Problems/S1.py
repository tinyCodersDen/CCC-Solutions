k = input()
l = ['C','D','H','S']
i = 1
l2 = []
a = ''
for t in k[1:]:
    if t==l[i]:
        l2.append(a)
        a = ''
        i+=1
        if i==len(l):
            i = 0
    else:
        a+=t
l2.append(a)
d = {'A':4,'K':3,'Q':2,'J':1}
print('Cards Dealt Points')
l3 = ['Clubs','Diamonds','Hearts','Spades']
p = 0
total = 0
for t in l2:
    s = 0
    for j in t:
        if j in d.keys():
            s+=d[j]
    if len(t)==0: s+=3
    if len(t)==1: s+=2
    if len(t)==2: s+=1
    total+=s
    print(l3[p]+' '+' '.join(t)+' '+str(s))
    p+=1
print('   Total',total)
