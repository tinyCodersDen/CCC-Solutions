N = int(input())
t = N//2
l = []
for a in range(N):
  l.append(int(input()))

ans = 0
for y in range(len(l)//2):
    if l[y] == l[y+t]:
        ans+=2
print(ans)
