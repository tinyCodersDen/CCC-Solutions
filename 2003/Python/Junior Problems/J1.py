t = int(input())
s = int(input())
h = int(input())
w = '*'+(' '*s)+'*'+(' '*s)+'*'
for q in range(t):
    print(w)
print('*'*len(w))
for k in range(h):
    print((' '*((len(w)-1)//2))+'*')
