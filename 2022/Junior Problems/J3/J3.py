import string
l = input()
l2 = []
alphabet = list(string.ascii_uppercase)
a = ''
for e,t in enumerate(l[:-1]):
    if t not in alphabet and l[e+1] in alphabet:
        a+=t
        l2.append(a)
        a = ''
    else:
        a+=t
a+=l[-1]
l2.append(a)
for t in l2:
    if '+' in t:
        t = t.split('+')
        print(t[0],'tighten',t[1])
    elif '-' in t:
        t = t.split('-')
        print(t[0],'loosen',t[1])
