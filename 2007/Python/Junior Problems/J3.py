u = int(input(''))
l = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
l2 = l.copy()
for q in range(u):
  l2.remove(l[int(input(''))-1])
dealer_amount = int(input(''))
mean = sum(l2)/len(l2)
if mean>dealer_amount:
  print('no deal')
else:
  print('deal')
