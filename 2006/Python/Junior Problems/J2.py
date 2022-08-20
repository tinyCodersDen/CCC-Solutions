r = int(input(''))
t = int(input(''))
ways = 0
for j in range(1,r+1):
  if j==10:
    break
  if 10-j<=t:
    ways+=1
if ways==1:
  print('There is 1 way to get the sum 10.')
else:
  print('There are',ways,'ways to get the sum 10.')
