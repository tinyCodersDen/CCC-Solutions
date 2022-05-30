l = []
for t in range(int(input(''))):
  l.append(int(input('')))
l.sort()
a = 10^100
for e,t in enumerate(l[1:-1]):
    n = ((l[e+2]-t)/2)+((t-l[e])/2)
    if n<a:
        a = n
print(a)
