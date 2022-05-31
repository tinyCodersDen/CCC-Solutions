start = int(input(''))
end = int(input(''))
ans = 0
for h in range(start,end+1):
  div = 0
  for n in range(1,h+1):
    if h%n==0:
      div+=1
  if div==4:
    ans+=1
print('The number of RSA numbers between',start,'and',end,'is',ans)
